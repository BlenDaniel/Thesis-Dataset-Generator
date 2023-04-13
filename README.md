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




### Parameter Descirptions:

task_id: None or Some identifier
| Value | Meaning |
| --- | --- |
| String | None or Some identifier |

task_message: 
| Value | Meaning |
| --- | --- |
| String | The description of task |

task_type:
| Value | Meaning |
| --- | --- |
| 1 | Feature requests or new feature |
| 2 | Bug fixes |
| 3 | Code Refactoring |
| 4 | Documentation |
| 5 | Testing |
| 6 | Deployment |
| 7 | Maintenance |
| 8 | Other |

has_bug_fixing: 
| Value | Meaning |
| --- | --- |
| 0 | Task doesn't include bug fixing |
| 1 | Task includes bug fixing | 

has_code_refactoring: 
| Value | Meaning |
| --- | --- |
| 0 | Task doesn't include code refactoring |
| 1 | Task includes code refactoring | 

is_fix_related: 
| Value | Meaning |
| --- | --- |
| 0 | Task is not fix related |
| 1 | Task is fix related | 

is_bug_fixing: 
| Value | Meaning |
| --- | --- |
| 0 | Task doesn't include bug fixing |
| 1 | Task includes bug fixing | 

is_refactoring: 
| Value | Meaning |
| --- | --- |
| 0 | Task is not refactoring |
| 1 | Task is refactoring | 

total_lines_added_in_commit: 
| Value | Meaning |
| --- | --- |
| Integer | Total lines added to the project | 

total_lines_deleted_in_commit: 
| Value | Meaning |
| --- | --- |
| Integer | Total lines deleted to the project | 

total_files_affected: 
| Value | Meaning |
| --- | --- |
| Integer | Total files affected by the commit | 

total_files_changed: 
| Value | Meaning |
| --- | --- |
| Integer | Total files changed with the addition and deletion of codes | 

author: 
| Value | Meaning |
| --- | --- |
| Integer | The index of the developer from the developers.csv | 

committer: 
| Value | Meaning |
| --- | --- |
| Integer | The index of the developer from the developers.csv | 

authored_at: 
| Value | Meaning |
| --- | --- |
| DateTime | Date and time value of when the commit was authored in the format DD/MM/YYYY, HH:MM:SS | 

authored_year: 
| Value | Meaning |
| --- | --- |
| Integer | Year of the task | 

commited_at: 
| Value | Meaning |
| --- | --- |
| DateTime | Date and time value of when the commit was committed in the format DD/MM/YYYY, HH:MM:SS | 

commited_year: 
| Value | Meaning |
| --- | --- |
| Integer | Year of the task was committed | 

commit_time: 
| Value | Meaning |
| --- | --- |
| 1 | 00:00-06:00AM |
| 2 | 06:00-12:00 |
| 3 | 12:00-18:00 |
| 4 | 18:00-23:59 |

auther_experience: 
| Value | Meaning |
| --- | --- |
| Integer | Authers experience in the company over the years they worked |

committer_experience: 
| Value | Meaning |
| --- | --- |
| Integer | Committers experience in the company over the years they worked |

code_quality: 
Calculates the code quality score based on the number of files affected, the number of files changed, the total 
lines added in the commit, the total lines deleted in the commit, the number of file additions and the number of 
file deletions, and whether the commit includes code refactoring. Returns a score between 0.0 and 5.0, rounded to 1 decimal place.
References are listed for the creating of the function.
| Value | Meaning |
| --- | --- |
| Integer | Quality calculated |

code_complexity: 
The calculate_code_complexity function takes in the following parameters: total_files_affected, total_files_changed, total_lines_added_in_commit, total_lines_deleted_in_commit, and has_bug_fixing. It calculates the McCabe's complexity metric using the radon.complexity module and adjusts the complexity metric if the commit includes bug fixing. The function then calculates the code complexity score by scaling the complexity metric to a range of 0.0 to 5.0. The function returns the calculated code complexity score.
| Value | Meaning |
| --- | --- |
| Integer | Complexity calculated |

communication: 
If the auther and committer were the same person, communication is estimated to be 0 or else 1.
| Value | Meaning |
| --- | --- |
| 0 | Author and Committer the same person. |
| 1 | Author and Committer are different. |

duration: 
Assumption: The Tasks are not done on all the same branch. They are merged in the `main` or `master` branch in the end.
But, the work commit steps were  not done there.

| Value | Meaning |
| --- | --- |
| Integer | Hours of the task, after once it was merged, did it need and update or not? This value return the hour difference between merge |


