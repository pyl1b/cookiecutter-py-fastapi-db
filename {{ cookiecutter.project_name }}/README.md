# {{ cookiecutter.project_slug }}

{{ cookiecutter.project_short_description }}

## Installation

```bash
python -m pip install {{ cookiecutter.project_slug }}
```

## Usage

TBD

## Development

Start by creating a virtual environment and installing the dependencies.
If you have a `make` command available, you can run `make init` after
the virtual environment is created and activated. Otherwise, you can run
the following commands:

```bash
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .[dev]
```

On Windows, to be able to serve the documentation, you may also need to
install the `cairo2` package:

```bash
pip install pipwin
pipwin install cairocffi
```
