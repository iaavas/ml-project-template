from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path, "r") as f:
      requirements =  [line.replace("\n", "") for line in f.readlines()]
      if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
      
    return requirements

setup(
  name="student_analysis",
  version="0.0.1",
  author="Aavash Baral",
  author_email="baralaavas@gmail.com",
  packages=find_packages(),
  install_requires=get_requirements("requirements.txt")
)