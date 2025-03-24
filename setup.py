from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-PROJECT-3",
    version="0.1",
    author="Naaz Nagori",
    packages=find_packages(),
    install_requires = requirements,
)