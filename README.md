**************************
ToDo - Command Line Tool
**************************

.. class:: no-web no-pdf

|Python| |Licence| |Build Status| |docs passing|


.. image::https://user-images.githubusercontent.com/82323267/122764927-9a0b0f00-d2bd-11eb-92ac-3c0ffe135605.png


Introduction
************
ToDo is command line task manager. It is a command line utility to add, delete, update and display the tasks. It is a powerful task manager written in Python. It uses SQLite3 database to store the tasks.


Features
********
* Add one Task at one time
* Display all Tasks in table format
* Remove a Task with specific ID
* Remove all Tasks
* Update a Task with a specific ID
* It uses offline


Dependencies
************
=============================================      ==================
     Features                                       Dependancy
=============================================      ==================
``Scripting Language``                              Python 3.0+
``Command-Line Option and argument parsing``        click
``Database Used``                                   SQLite3
``Display Bookmarks in Table``                      tabulate
=============================================      ==================

Installation
************
ToDo is installed using setup.py file:

.. code-block:: bash

    python setup.py install

Command line options
********************
.. code-block:: bash

    Usage: ToDo [OPTIONS] [INSERT]...

      ToDo - Command-line Task manager tool.

    Options:
    -a, --add TEXT...       Add the Task 
    -d, --delete TEXT       Remove a Task of particular ID
    -u, --update TEXT...    Update a Task for specific ID
    -s, --show TEXT...      Show all Tasks
    --help                  Show this message and exit.


Examples
********
1. **Add** the Tasks:

.. code-block:: bash

    $ todo add --add "task" ...
    or
    $ todo add -a "task" ...

2. **Show** all added tasks:

.. code-block:: bash

    $ todo -s
    or
    $ todo --show

3. **Update** a task using its ID:

.. code-block:: bash

    $ todo update

4. **Delete** todo delete ID:

.. code-block:: bash

    $ todo delete

How to install source code for development
**********************************************
* Clone project from github:

.. code-block:: bash

    $ git clone https://github.com/kasul092/todo.git

* We recommend to create and activate a virtualenv first:

.. code-block:: bash

    $ cd todo/

    $ py -m virtualenv env

    $ env/Scripts/activate

    (env) $

* To install using setup.py file:

.. code-block:: bash

        (env) $ python setup.py install


************************************************************************
`Licence <https://github.com/kasul092/todo/blob/main/LICENSE>`_
************************************************************************
ToDo - Command line tool is licensed under `GNU General Public License v3.0. <https://github.com/kasul092/todo/blob/main/LICENSE>`_

.. |Python| image:: https://img.shields.io/badge/python-3.6-blue.svg

.. |Licence| image:: https://img.shields.io/badge/license-MIT-yellow.svg?maxAge=2592000
    :target: https://github.com/projectreadit/readit/blob/master/LICENSE

