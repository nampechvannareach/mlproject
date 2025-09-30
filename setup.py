from setuptools import find_packages,setup
from typing import List

def get_requirement(file_path:str)->List[str]:
    requirements=[]
    with open('requirement.txt') as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n","") for req in requirements]
setup(
    name='mlproject',
    version='0.0.1',
    author='nampechvannareach',
    author_email='reachnam762@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirement.txt')
)