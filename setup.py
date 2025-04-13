from setuptools import setup, find_packages

setup(
    name="custom-terminal",  # PyPI package name (must be unique)
    version="0.1.0",        # Update for each release
    packages=find_packages(),
    install_requires=["requests"],  # List dependencies
    entry_points={
        'console_scripts': [
            'cterm=custom_terminal.main:main',  # CLI command
        ],
    },
    author="Harmandeep Singh",
    description="A custom terminal with weather commands",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HarmandeepSinghDhillon/Custom-Terminal.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)