.PHONY: install run test lint

BIN = docker run \
			--interactive \
			--rm \
			-v "/code" \
			--name reversi-python-running \
			reversi-python

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
