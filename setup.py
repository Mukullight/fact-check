from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="fact-check",  # Changed to match your project name
    version="0.0.1",
    author="Mukulnamagiri",
    author_email="mukulnamagiri1@gmail.com",
    description="fact-checker of video transcriptions using large language models",  # Added a description
    long_description=open("README.md").read(),  # Added long description
    long_description_content_type="text/markdown",  # Specified content type for long description
    url="https://github.com/mukullight/fact-check",  # Add your GitHub repo URL
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.12.0",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',  # Specify minimum Python version
)