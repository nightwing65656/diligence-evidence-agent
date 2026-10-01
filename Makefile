.PHONY: install test lint type check

install:
	python -m pip install -U pip
	python -m pip install -e .
	python -m pip install pytest ruff mypy

test:
	python -m pytest -q

lint:
	ruff check .

type:
	mypy src/diligence_agent

check: lint type test
