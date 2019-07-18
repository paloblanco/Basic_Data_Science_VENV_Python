# Basic Python Virtual Environment For Data Science

The purpose of this repo is to provide you with a basic sandbox virtual environment for data science. After setting up this environment, you will have some basic convenience scripts setup to allow you to easily use jupyter lab to write python code.

## Requirements

You must have python installed on your machine and added to path. You can check to see that python is accessible via path by opening a cmd/shell and typing thhe following:

    python -V

You should get a prompt telling you what version of python is involved. If you do not get a prompt, you either need to make sure python is installed, or add the following items to PATH (note that you should adjust the paths below to match your machine):

    C:\Users\<user>\AppData\Local\Programs\Python\Python37\Scripts\
    C:\Users\<user>\AppData\Local\Programs\Python\Python37\

Once you are able to check the python version, you are good to go.

## Setup

1. Clone this repo to a folder on your computer. You can also just download it and extract it where you plan on working. I recommend making a directory such as C:/src/datascisandbox, but you can put it anywhere as long as it is not shared with other documents (don't put all of the items directly into my documents, for example).

2. Double-click bootstrap_python_venv.bat. This will perform the following steps for you.
    a. Use python to create a virtual environment (named "venv")
    b. Install some baseling packages that you will need to get started, including numpy, pandas, jupyter, and matplotlib.

## Description of contents

...