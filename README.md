# Useable Data Generator

This is a repository to generate useable data from any github project. 

1. Requirements
    - CSV: 
        CSV datasheet of the history of the repository. 
    - JSON:
        Json of the history of the repository. 

2. Steps to produce and what the outputs are:
    | Step | Description | Input | Output |
    | --- | --- | --- | --- |
    | 1 | Get a list of all the developers associated with the project | CSV (data sheet of the history of the repository) | CSV |
    | 2 | Get developers experience over the years since the creation date of the project. | CSV (data sheet of the history of the repository), JSON (the history of the repository) | CSV |
    | 3 | Get developers authering of a task over the years since the creation date of the project. | CSV (data sheet of the history of the repository), JSON (the history of the repository) | CSV |
    | 4 | Get developers commit or provisioning of a task over the years since the creation date of the project. | CSV (data sheet of the history of the repository), JSON (the history of the repository) | CSV |
    | 5 |  Getting task information | JSON (the history of the repository), CSV (getting the output of developers experience (2nd Step)) | CSV |
    | 6 | Setting task information | CSV (getting the output of tasks (5th Step)) | CSV |


<hr>


## Installation Guides

For the proper functioning of the application, you need to have python3 and pip3 installed. You can find python installation guide [here](https://www.python.org/downloads/) and pip installation guide [here](https://pip.pypa.io/en/stable/installation/). \
Once python and pip are installed, there are various python modules that are also required. \
<br>

## Procedure for running the flask-app
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






## Tests
To run the test cases, you need to be in the virtual environment and also have your cache system running. 
<br>

## For starting the virtual environment.

    pipenv shell


### To setup:

    pip3 install .


### To run tests:

    pytest

