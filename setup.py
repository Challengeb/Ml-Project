from setuptools import find_packages, setup
from typing import List
HYPHEN_E_DOT = "-e ."
def get_requirements(file_path: str) -> list:
    """This function will return the list of requirements"""
    with open(file_path) as requirement_file:
        return [req.strip() for req in requirement_file.readlines() if req.strip() and not req.startswith(HYPHEN_E_DOT)]
        

setup(
    name="ml_project", 
    version="0.1.0",
    author="Challenge Bhongwani",
    author_email="challengebhongwani@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")  
)