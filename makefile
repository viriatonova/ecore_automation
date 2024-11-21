SHELL := /bin/bash
.SILENT:
.DEFAULT_GOAL := help

.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: setup 
setup: ## Install project dependencies
	python -m pip install requirements.txt

.PHONY: compile 
compile: ## Compile project dependencies
	pip-compile --strip-extras --extra dev -o requirements.txt pyproject.toml

.PHONY: update 
update: ## Update project dependencies
	pip-sync requirements.txt

.PHONY: lint 
lint: ## Lint project
	ruff check . --fix

.PHONY: test
test: ## Run tests with debug
	PWDEBUG=1 pytest -s

.PHONY: only
only: ## Run tests marked only
	pytest -m only

.PHONY: e2e
e2e: ## Run end-to-end tests
	pytest -m e2e
