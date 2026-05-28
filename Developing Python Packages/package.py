from setuptools import setup, find_packages

setup(
    name="impyrial",
    version="0.1.0",
    author="Austin",
    description="A package for converting impyrial lengths and weights.",
    packages=find_packages(include=["impyrial", "impyrial.*"])
)