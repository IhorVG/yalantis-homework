.PHONY: setup \
		mypy \
		help

venv/bin/activate: ## Alias for virtual environment
	python -m venv venv

mypy: venv/bin/activate ## Run mypy
	. venv/bin/activate; mypy ./

# Just help
help: ## Display help screen
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
