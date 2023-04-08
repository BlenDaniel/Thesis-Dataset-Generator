# Parser

<hr>

## Introduction



# Installation Guides

For the proper functioning of the application, you need to have python3 and pip3 installed. You can find python installation guide [here](https://www.python.org/downloads/) and pip installation guide [here](https://pip.pypa.io/en/stable/installation/). \
Once python and pip are installed, there are various python modules that are also required. \
<br>

# Procedure for running the flask-app
### Install a virtual machine

    pip3 install pipenv

Once it's installed, you can create a virtual environment and activate it using this command:

### Start the virtual environment.

    pipenv shell

### Install all the dependencies

    pipenv install -r requirements/requirements.txt

### To setup all the modules and paths

    pip3 install .


### Add the model
    python -m spacy download en_core_web_sm


###  To deactivate the virtual environment, you can use this command:

    exit





# Tests
To run the test cases, you need to be in the virtual environment and also have your cache system running. 
<br>

## For starting the virtual environment.

    pipenv shell


### To setup:

    pip3 install .


### To run tests:

    pytest

