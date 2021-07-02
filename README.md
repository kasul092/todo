
# MyTask - Command Line Tool


![alt text][Python]  ![alt text][license]


![alt text][logo]

[logo]:https://user-images.githubusercontent.com/82323267/124240926-e31e5700-db38-11eb-9125-26ed3b21442b.png


## Introduction

MyTask is command line task manager. It is a command line utility to add, delete, update and display the tasks. It is a powerful task manager written in Python. It uses SQLite3 database to store the tasks.


## Features

* Add one Task at one time
* Display all Tasks in table format
* Remove a Task with specific ID
* Remove all Tasks
* Update a Task with a specific ID
* It uses offline


## Dependencies

| Features | Dependancy |
|---|---|
| ``Scripting Language`` | Python 3.0+
| ``Command-Line Option and argument parsing`` | click
| ``Database Used`` | SQLite3
| ``Display Bookmarks in Table`` | tabulate |


## Installation

MyTask is installed using setup.py file:



    python setup.py install

## Command line options


    Usage: MyTask [OPTIONS] [INSERT]...

      MyTask - Command-line Task manager tool.

    Options:
    -a, --add TEXT...       Add the Task 
    -d, --delete TEXT       Remove a Task of particular ID
    -u, --update TEXT...    Update a Task for specific ID
    -s, --show TEXT...      Show all Tasks
    --help                  Show thismessage and exit.


## Examples

### 1. **Add** the Tasks:


     $ mytask add --add "task" ...
     
     or
     
    $ mytask add -a "task" ...



### 2. **Show** all added tasks:


     $ mytask -s
  
      or
     
     $ mytask --show

### 3. **Update** a task using its ID:



    $ mytask update

### 4. **Delete** a task using its ID:

    $ mytask delete

## How to install source code for development

* Clone project from github:



      $ git clone https://github.com/kasul092/todo.git

* We recommend to create and activate a virtualenv first:

   

       $ cd mytask/

      $ py -m virtualenv env

      $ env/Scripts/activate

      (env) $

* To install using setup.py file:



       (env) $ python setup.py install



MyTask - Command line tool is licensed under [MIT License](https://github.com/kasul092/todo/blob/main/LICENSE)





[Python]:https://img.shields.io/badge/python-3.6-blue.svg



[license]:https://img.shields.io/badge/license-MIT-yellow.svg?maxAge=2592000


