# {{cookiecutter.project_name}}

- [{{cookiecutter.project_name}}](#cookiecutterprojectname)
  - [Usage](#usage)
  - [Install](#install)

## Usage

```bash
{{cookiecutter.project_name}} --help
```

## Install

```bash
# create a venv
virtualenv -p python3.7 venv

# activate the venv
source venv/bin/activate

# install dependencies
poetry install
```

To bundle your script with setuptools for dev purposes run:

```bash
pip install --editable .
```

To setup the script to run from any directory, run this in your home directory:

```
pip3 install --editable /Users/{username}/path/to/{{cookiecutter.project_name}}
```
