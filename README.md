# json-splitter
A command line tool for splitting large JSON files into smaller JSON files based on the preferred number of records per file. Python 3+ required.

## Table of Contents

- [json-splitter](#json-splitter)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)

## Installation
This script requires Python to be installed on the local machine. Please visit [Python.org](https://www.python.org/) to install or type `python3 --version` to verify it is already installed.

Once Python is installed, clone the project (https://github.com/AmpleOpportunity/json-splitter.git) or download the ZIP file and extract manually.

## Usage
Place a JSON file within the same directory as the script. The JSON file must be an Array of Objects or Multidimensional Array.

Navigate to the directory where the script exists and begin by typing `python3 json-splitter.py`

Enter the name of the JSON file (include the extension) when prompted, then enter the maximum number of records for each file.

The script will complete and equally split the JSON file into the appropriate number of files to stay under the maximum size.
