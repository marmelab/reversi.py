.PHONY: install run test lint

# Initialization ===============================================================

install:
	docker build --tag=reversi-python .

# Run ===============================================================

run:
	docker run \
		--interactive \
		--rm \
		-v "/code" \
		--name reversi-python-running \
		reversi-python ./src/reversi.py

# Tests ===============================================================

test:
	python -m unittest discover

# Lint ===============================================================

lint:
	pep8 .
