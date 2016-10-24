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
	 $(BIN) bash -c "./src/reversi.py"

# Tests ===============================================================

test:
	$(BIN) bash -c "python -m unittest discover"

# Lint ===============================================================

lint:
	$(BIN) bash -c "pep8 . --max-line-length=150"
