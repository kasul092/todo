from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name = "ToDo",
    version = "0.0.9",
    description = "Todo manager tool",
    long_description = readme,
    url = "https://github.com/kasul092/todo",
    author  = "Sumit Pujari",
    author_email = "sumitpujari199723@gmail.com",
    packages = find_packages(include=["todo"]),
    python_requires ='>=3.6',
    install_requires = ['click'],
    entry_points = {
        "console_scripts":[
            "todo=todo:main",
        ],
    },
)