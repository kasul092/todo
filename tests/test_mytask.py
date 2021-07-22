
from mytask import task as t

# Testing --help option
def test_help_option():
    """testing the help of mytask"""
    expected_output = (
        "Usage: main [OPTIONS] [INSERT]...\n"
        "\n"
        "  Mytask - Command-line task manager tool."
        "\n\n"
        "Options:\n"
        "-a, --add TEXT...       Add the Task\n" 
        "-d, --delete TEXT...    Remove a Task of particular ID\n"
        "-u, --update TEXT...    Update a Task for specific ID\n"
        "-s, --show TEXT...      Show all Tasks\n"
        "-c, --clear TEXT...     Clear all the tasks present in table\n"
        "-st, --status TEXT...   Provide a status to the task\n"
        "-o, --sort TEXT...      Sort the task by date\n"
    )
