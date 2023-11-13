# Basic Python Virtual Environment For Data Science

The purpose of this repo is to provide you with a basic sandbox virtual environment for data science. After setting up this environment, you will have some basic convenience scripts setup to allow you to easily use jupyter lab to write python code.

## Requirements

You must have python installed on your machine and added to path. You can check to see that python is accessible via path by opening a cmd/shell and typing the following:

    python -V

You should get a prompt telling you what version of python is installed. If you do not get a prompt, you either need to make sure python is installed, or add the following items to PATH (note that you should adjust the paths below to match your machine):

    C:\Users\<user>\AppData\Local\Programs\Python\Python37\

Once you are able to check the python version, you are good to go.

## Setup

1. Clone this repo to a folder on your computer. You can also just download it and extract it where you plan on working. I recommend making a directory such as C:/src/datascisandbox, but you can put it anywhere as long as it is not shared with other documents (don't put all of the items directly into my documents, for example).

2. Double-click bootstrap_python_venv.bat. This will perform the following steps for you.
    1. Use python to create a virtual environment (named "venv"). Think of this like a project - you can have one directory containing a "venv" folder per major software project. If you are just using python to explore data and write some small scripts, you will probably only need one directory.
    2. Install some baseling packages that you will need to get started, including numpy, pandas, jupyter, and matplotlib.

## Description of contents

This repo comes with several batch scipts that will let you get started and go quite far with python.

- **start_jupyter_lab.bat** - this will start jupyter lab. This is the best way to get started with writing data science code in python.
- **start_venv.bat** - This is important. If you want to do anything on the command line with this environment, such as using pip to install new packages, you need to start here. This will activate the virtual environment, which essentially sets up a shell with a lot of temporary environment variables set so that you only play in this environment. If you need to install a new package, start here.
    - for example, to install "bokeh," you would doubleclick "start_venv.bat", then type the following:
        ```
        python -m pip install bokeh
        ```
    - you should also use this script if you plan on running anything on the command line, like starting a python shell or running a standalone script.
- **start_idle.bat** - IDLE is a small text editor that comes bundled in python. It is similar to "notepadd++", but is geared specifically for python. This batch script will start it. If you are just getting started, I recommend using jupyter lab to write code instead. If you are writing a lot of scripts for automation, you may want to upgrade to a more fully-featured editor, like PyCharm or VSCode.
- **requirements.txt** - This is a list of requirements that python will install into this environment. If you need a new requirement, you can install it with pip.
- **bootstrap_python_venv.bat** - sets up a virtual environment and installs requirements. If you somehow mess up your environment or install a bad package, you can delete the "venv" folder and make it again by running this script. None of your python scripts or notebooks will be deleted.
- **install_requirements.bat** - will install requirements without setting up an environment.