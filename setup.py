from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_nazgulll",
    version="0.0.3",
    author="Felipe",
    author_email="felipelean@hotmail.com",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FelipeBorba87/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
)
