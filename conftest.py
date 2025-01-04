#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
This script configures markers on tests based on filenames for CircleCI parallelization.
It is used to split up tests into different CircleCI runs.
"""

import os
import pathlib
import random
import collections
import pytest
import subprocess


# -----------------------------------------------------------------------
# From https://github.com/ryanwilsonperkin/pytest-circleci-parallelized.
# MIT licensed, Copyright Ryan Wilson-Perkin.
# -----------------------------------------------------------------------

def get_class_name(item):
    """Extract the class name from a pytest item."""
    class_name, module_name = None, None
    for parent in reversed(item.listchain()):
        if isinstance(parent, pytest.Class):
            class_name = parent.name
        elif isinstance(parent, pytest.Module):
            module_name = parent.module.__name__
            break

    # Heuristic: group GPU and task tests, as they are likely to share caching
    if class_name and '.tasks.' not in module_name:
        return f"{module_name}.{class_name}"
    else:
        return module_name


def filter_tests_with_circleci(test_list):
    """Split tests using CircleCI's split functionality."""
    circleci_input = "\n".join(test_list).encode("utf-8")
    p = subprocess.Popen(
        ["circleci", "tests", "split"], stdin=subprocess.PIPE, stdout=subprocess.PIPE
    )
    circleci_output, _ = p.communicate(circleci_input)
    return [
        line.strip() for line in circleci_output.decode("utf-8").strip().split("\n")
    ]


# Define marker rules for different test categories
MARKER_RULES = [
    ('parlai_internal', 'internal'),
    ('crowdsourcing/', 'crowdsourcing'),
    ('nightly/gpu', 'nightly_gpu'),
    ('nightly/cpu/', 'nightly_cpu'),
    ('datatests/', 'data'),
    ('parlai/tasks/', 'teacher'),
    ('tasks/', 'tasks'),
    ('tod/', 'tod'),
]

def pytest_collection_modifyitems(config, items):
    """
    Modify the test items by adding appropriate markers based on filename patterns.
    Also, handle test filtering and splitting for CircleCI parallelization.
    """
    marker_expr = config.getoption('markexpr')
    deselected = []

    rootdir = pathlib.Path(config.rootdir)
    
    # Apply markers based on filename patterns
    for item in items:
        rel_path = str(pathlib.Path(item.fspath).relative_to(rootdir))
        marker_assigned = False
        for file_pattern, marker in MARKER_RULES:
            if file_pattern in rel_path:
                item.add_marker(marker)
                marker_assigned = True
                if marker_expr and marker != marker_expr:
                    deselected.append(item)
                break
        
        if not marker_assigned:
            assert "/" not in rel_path[6:], f"Couldn't categorize '{rel_path}'"
            item.add_marker("unit")
            if marker_expr not in ['', 'unit']:
                deselected.append(item)

    # Remove deselected items
    for item in deselected:
        items.remove(item)

    if 'CIRCLE_NODE_TOTAL' in os.environ:
        # Split tests into groups based on class name for CircleCI parallelism
        class_mapping = collections.defaultdict(list)
        for item in items:
            class_name = get_class_name(item)
            class_mapping[class_name].append(item)

        test_groupings = list(class_mapping.keys())
        random.Random(1339).shuffle(test_groupings)

        filtered_tests = filter_tests_with_circleci(test_groupings)
        new_items = []
        for name in filtered_tests:
            new_items.extend(class_mapping[name])
        items[:] = new_items


def pytest_sessionfinish(session, exitstatus):
    """
    Ensure that pytest doesn't report failure when no tests are collected, 
    which can happen during test distribution across CircleCI nodes.
    """
    if exitstatus == pytest.ExitCode.NO_TESTS_COLLECTED:
        session.exitstatus = pytest.ExitCode.OK
