MODULE_NAME ?= {{ cookiecutter.project_slug }}
PACKAGE_NAME ?= {{ cookiecutter.project_name }}
CONFIG_FILE ?= {{ cookiecutter.project_slug }}/server/default-config.yaml
ifeq ($(OS),Windows_NT)
    detected_OS := Windows
else
    detected_OS := $(shell uname)
endif
ifeq ($(OS),Windows_NT)
	RMRF = rmdir /s /q
else
	RMRF = rm -rf
endif

export {{ cookiecutter.env_prefix }}_CONFIG=$(CONFIG_FILE)


init:
	python -m pip install --upgrade pip
	python -m pip install -e .[dev]
	python -m pip install -e .[server]
	python -m pip install -e .[docs]
	pre-commit install


run:
	python \
		-m uvicorn $(MODULE_NAME).server.main:app \
		--reload \
		--port {{ cookiecutter.port }}


all: test build-dist build-docs


sdist:
	$(RMRF) dist || echo "dist not found, skipping"
	$(RMRF) build || echo "build not found, skipping"
	$(RMRF) $(MODULE_NAME).egg-info || echo "egg-info not found, skipping"
	python -m build
	python -m twine check dist/*


lint:
	@python -m isort --check $(MODULE_NAME)  ||  echo "isort:   FAILED!"
	@python -m black --check --quiet $(MODULE_NAME) || echo "black:   FAILED!"
	@python -m pflake8 $(MODULE_NAME)  || echo "flake8:  FAILED!"


delint:
	python -m isort $(MODULE_NAME)
	python -m black $(MODULE_NAME)


typecheck:
	python -m mypy $(MODULE_NAME)


test: lint typecheck
	python -m pytest \
		--cov-report term \
		--cov-report html \
		--cov-config=.coveragerc \
		--cov=$(MODULE_NAME) $(MODULE_NAME)/

build-dist:
	python -m build


build-docs:
	python -m mkdocs build


view-docs:
	python -m mkdocs serve
