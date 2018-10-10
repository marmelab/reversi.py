.PHONY: install run test lint

BIN = docker run \
			--interactive \
			--rm \
			-v "/code" \
			--name reversi-python-running \
			reversi-python

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# Initialization ===============================================================

install:
	docker build --tag=reversi-python .

# Run ===============================================================

run:
	 $(BIN) ./src/reversi.py

# Tests ===============================================================

test:
	$(BIN) python -m unittest discover

# Lint ===============================================================

lint:
	$(BIN) pep8 . --max-line-length=150
