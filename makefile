SHELL := /bin/bash
.SILENT:
.DEFAULT_GOAL := help

.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)


.PHONY: setup
setup:
	python -m pip install requirements.txt

.PHONY: compile
compile:
	pip-compile --strip-extras --extra dev -o requirements.txt pyproject.toml

.PHONY: update
update:
	pip-sync requirements.txt
