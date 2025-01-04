<p align="center">
  <img src="docs/source/_static/img/parlai.png" alt="ParlAI Logo" style="max-width: 70%; width: 100%; height: auto;" />
</p>

<p align="center">
  <a href="https://github.com/facebookresearch/ParlAI/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License" />
  </a>
  <a href="https://pypi.org/project/parlai/">
    <img src="https://img.shields.io/pypi/v/parlai?color=blue&label=release" alt="ParlAI Version" />
  </a>
  <a href="https://circleci.com/gh/facebookresearch/ParlAI/tree/main">
    <img src="https://img.shields.io/circleci/build/github/facebookresearch/ParlAI/main" alt="CircleCI Build Status" />
  </a>
  <a href="https://codecov.io/gh/facebookresearch/ParlAI">
    <img src="https://img.shields.io/codecov/c/github/facebookresearch/ParlAI" alt="Code Coverage" />
  </a>
  <a href="https://img.shields.io/github/contributors/facebookresearch/ParlAI">
    <img src="https://img.shields.io/github/contributors/facebookresearch/ParlAI" alt="GitHub Contributors" />
  </a>
  <a href="https://twitter.com/parlai_parley">
    <img src="https://img.shields.io/twitter/follow/parlai_parley?label=Twitter&style=social" alt="Follow ParlAI on Twitter" />
  </a>
</p>

<hr />

<p style="text-align: center;">
  <a href="http://parl.ai">
    <img src="https://raw.githubusercontent.com/facebookresearch/ParlAI/main/docs/source/_static/img/parlai_example.png" alt="ParlAI Example" style="max-width: 90%; width: 100%; height: auto;" />
  </a>
</p>

<h2>Interactive Tutorial</h2>
<p>For those who want to start with ParlAI now, you can try our <a href="https://colab.research.google.com/drive/1bRMvN0lGXaTF5fuTidgvlAl-Lb41F7AD#scrollTo=KtVz5dCUmFkN">Colab Tutorial</a>.</p>

<h2>Installing ParlAI</h2>
<h3>Operating System</h3>
<p>ParlAI should work as intended under Linux or macOS. Windows is not officially supported, but many users have reported success with Python 3.8. We welcome patches to improve Windows support.</p>

<h3>Python Interpreter</h3>
<p>ParlAI requires Python 3.8 or higher.</p>

<h3>Requirements</h3>
<p>ParlAI supports <a href="https://pytorch.org">Pytorch</a> 1.6 or higher. For a full list of requirements, refer to <a href="https://github.com/facebookresearch/ParlAI/blob/main/requirements.txt">requirements.txt</a>. Some models may have additional requirements.</p>

<h3>Virtual Environment</h3>
<p>We strongly recommend installing ParlAI in a virtual environment. You can use either <a href="https://docs.python.org/3/library/venv.html">venv</a> or <a href="https://www.anaconda.com/">conda</a>.</p>

<h3>End User Installation</h3>
<p>If you want to use ParlAI without modifications, follow these steps:</p>
<pre>
cd /path/to/your/parlai-app
python3.8 -m venv venv
venv/bin/pip install --upgrade pip setuptools wheel
venv/bin/pip install parlai
</pre>

<h3>Developer Installation</h3>
<p>If you want to modify parts of ParlAI, set up a development environment with:</p>
<pre>
git clone https://github.com/facebookresearch/ParlAI.git ~/ParlAI
cd ~/ParlAI
python3.8 -m venv venv
venv/bin/pip install --upgrade pip setuptools wheel
venv/bin/python setup.py develop
</pre>
<p><strong>Note:</strong> If the installation fails, try building a fresh conda environment with:</p>
<pre>
conda install pytorch==2.0.0 torchvision torchaudio torchtext pytorch-cuda=11.8 -c pytorch -c nvidia
</pre>

<h2>Documentation</h2>
<ul>
  <li><a href="https://parl.ai/docs/tutorial_quick.html">Quick Start</a></li>
  <li><a href="https://parl.ai/docs/tutorial_basic.html">Basics: world, agents, teachers, actions, and observations</a></li>
  <li><a href="http://parl.ai/docs/tutorial_task.html">Creating a new dataset/task</a></li>
  <li><a href="https://parl.ai/docs/agents_list.html">List of available agents</a></li>
  <li><a href="https://parl.ai/docs/zoo.html">Model zoo (list pretrained models)</a></li>
  <li><a href="http://parl.ai/docs/tutorial_crowdsourcing.html">Running crowdsourcing tasks</a></li>
  <li><a href="https://parl.ai/docs/tutorial_chat_service.html">Plug into Facebook Messenger</a></li>
</ul>

<h2>Examples</h2>
<p>A large set of scripts can be found in <a href="https://github.com/facebookresearch/ParlAI/tree/main/parlai/scripts">parlai/scripts</a>. Here are a few examples:</p>
<p>Display 10 random examples from the SQuAD task:</p>
<pre>parlai display_data -t squad</pre>

<p>Evaluate an IR baseline model on the validation set of the Personachat task:</p>
<pre>parlai eval_model -m ir_baseline -t personachat -dt valid</pre>

<p>Train a single-layer transformer on PersonaChat (requires pytorch and torchtext):</p>
<pre>parlai train_model -t personachat -m transformer/ranker -mf /tmp/model_tr6 --n-layers 1 --embedding-size 300 --ffn-size 600 --n-heads 4 --num-epochs 2 -veps 0.25 -bs 64 -lr 0.001 --dropout 0.1 --embedding-type fasttext_cc --candidates batch</pre>

<h2>Code Organization</h2>
<p>The code is organized into the following main directories:</p>
<ul>
  <li><a href="https://github.com/facebookresearch/ParlAI/tree/main/parlai/core">core</a>: Primary code for the framework</li>
  <li><a href="https://github.com/facebookresearch/ParlAI/tree/main/parlai/agents">agents</a>: Agents that interact with various tasks</li>
  <li><a href="https://github.com/facebookresearch/ParlAI/tree/main/parlai/scripts">scripts</a>: Useful scripts for training, evaluating, chatting, etc.</li>
  <li><a href="https://github.com/facebookresearch/ParlAI/tree/main/parlai/tasks">tasks</a>: Code for available tasks in ParlAI</li>
  <li><a href="https://github.com/facebookresearch/ParlAI/tree/main/parlai/mturk">mturk</a>: Code for setting up Mechanical Turk</li>
  <li><a href="https://github.com/facebookresearch/ParlAI/tree/main/parlai/chat_service/services/messenger">messenger</a>: Interface with Facebook Messenger</li>
  <li><a href="https://github.com/facebookresearch/ParlAI/tree/main/parlai/utils">utils</a>: Utility methods</li>
  <li><a href="https://github.com/facebookresearch/ParlAI/tree/main/parlai/crowdsourcing">crowdsourcing</a>: Code for running crowdsourcing tasks</li>
  <li><a href="https://github.com/facebookresearch/ParlAI/tree/main/parlai/chat_service/services/messenger">chat_service</a>: Interfaces with chat services like Messenger</li>
  <li><a href="https://github.com/facebookresearch/ParlAI/tree/main/parlai/zoo">zoo</a>: Downloads and uses pretrained models</li>
</ul>

<h2>Support</h2>
<p>If you have questions or need support, feel free to post on our <a href="https://github.com/facebookresearch/ParlAI/issues">Github Issues page</a>. You can also refer to our <a href="https://parl.ai/docs/faq.html">FAQ</a> and <a href="https://parl.ai/docs/tutorial_tipsntricks.html">Tips n Tricks</a>.</p>

<h2>Contributing</h2>
<p>We welcome contributions! For information on how to contribute to ParlAI, refer to our <a href="https://github.com/facebookresearch/ParlAI/blob/main/CONTRIBUTING.md">Contributing Guide</a>.</p>

<h2>The Team</h2>
<p>ParlAI is developed by the Facebook AI Research team. For details on the team members, refer to the <a href="https://github.com/facebookresearch/ParlAI/blob/main/README.md#authors">Authors</a> section.</p>
