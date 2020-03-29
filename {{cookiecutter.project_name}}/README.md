# {{cookiecutter.project_name}}

<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

- [{{cookiecutter.project_name}}](#cookiecutterprojectname)
  - [Usage](#usage)
  - [Dev Install](#dev-install)
  - [Global Install](#global-install)

## Usage

```bash
{{cookiecutter.project_name}} --help
```

## Dev Install

```bash
# create a venv
virtualenv -p python{{cookiecutter.python_version}} venv

# activate the venv
source venv/bin/activate

# install dependencies
poetry install
```

## Global Install

To use the CLI app globally, use `pipx` to install in an isolated environment. Refer to the [pipx docs](https://pipxproject.github.io/pipx/) for more info.

```bash
pipx install git+https://github.com/<user-name>/{{cookiecutter.project_name}}
```
