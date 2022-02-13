<h1 align="center">
    <img src="https://raw.githubusercontent.com/talwat/py-load/main/svgs/py-load-logo.svg" width="30%">
</h1>
<h1 align="center">
    Py-Load
</h1>
<h2 align="center">
    A super simple, compact, and easy to use loading bar module for python with no dependencies.
</h2>

[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/talwat/py-load.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/talwat/py-load/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/talwat/py-load.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/talwat/py-load/alerts/)
[![Build](https://img.shields.io/github/workflow/status/talwat/py-load/Python%20application)](https://github.com/talwat/py-load/actions/workflows/python-app.yml)
[![License](https://img.shields.io/github/license/talwat/py-load)](https://github.com/talwat/py-load/blob/main/LICENSE)
[![Code Size](https://img.shields.io/github/languages/code-size/talwat/py-load)](https://img.shields.io/github/languages/code-size/talwat/py-load)
[![PyPi Version](https://img.shields.io/pypi/v/py-load-lib)](https://pypi.org/project/py-load-lib)
[![Commits](https://img.shields.io/github/commit-activity/m/talwat/py-load)](https://github.com/talwat/py-load/commits/main)
[![Last Commit](https://img.shields.io/github/last-commit/talwat/py-load)](https://github.com/talwat/py-load/commits/main)
[![Stars](https://img.shields.io/github/stars/talwat/py-load)](https://img.shields.io/github/stars/talwat/py-load)

## Quick Start

You can super quickly make a loading bar by using Smartbars like so:

```python
from py_load import *

for i in Smartbar(range(1000)):
    # do stuff
print("Done!")
```

## Info

### Other Loading Bars

Py-load isn't the best option for style or for features. Py-load is meant to be simple, not flashy.

It's also just one dude working on it, so it's harder to maintain.

If you want a more complex *Codebase Wise* but well documented and fleshed out use [tqdm](https://github.com/tqdm/tqdm).

If you want something that looks absolutely awesome, use [alive-progress](https://github.com/rsalmei/alive-progress)
*Seriously their bars look really cool!*

### Py-load

Py-load is a simple python package that allows you to very easily add loading bars to your CLI app.

Py-load is very lightweight, and requires no other dependencies, and is also fairly customizable.

It uses modern python features to make the code organized and maintainable.

This whole repository is some what of a learning project.
So I may goof up every now and then since I am not very experienced with Github and all of its features.

That's why you may see some strange commits every now and then. Sorry!

*Note: I will do my best to keep the **code** itself clean and organized*

## Requirements

Py-load only needs [Python](https://python.org) 3.6 or higher, as it uses Python 3 features.

### Tested Python Versions

* 3.10
* 3.9
* 3.8

## Installing

### Installing from source

Download `py_load.py` and put it in your projects source folder, and then your done!

This will give you the newest features, but it may be unstable.

### Installing with Pip

You can also use pip to install it by doing `pip install py-load-lib`

This will usually be fairly stable and robust, however it is updated a little slower.

## Usage

See the [Wiki](https://github.com/talwat/py-load/wiki) for info on usage.

## Credits

Contributors:

* Talwat *(creator/lead maintainer)*
* Nobody else for now :(

## Contributing

If you want to contribute you can either open a PR or you can open an issue.

Some useful things you could do is:

* Test py-load with different python 3 versions

* Suggest new features

* Contribute code and fix bugs
