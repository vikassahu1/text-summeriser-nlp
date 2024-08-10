import os
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

# This thing will create whole project stucture 
project_name = "textSummererProject"
list_of_files = [
    ".github/workflows/.gitkeep",  # used during cicd pipelines 
    f"src/{project_name}/__init__.py", #to perform local import operations we need to install this as a local package
    f"src/{project_name}/components/__init__.py", # another local package and its constructor
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py"
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
     "config/config.yaml",     #yaml contains parameters we are going to use 
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

#basically all the things we need are in template files