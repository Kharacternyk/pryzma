debug: black flake pytest
	@python -q

black:
	@black pryzma/* tests/* 2>&1 | tail -n1

flake:
	@flake8 pryzma/* tests/*

pytest: export PYTHONPATH = ../pryzma
pytest:
	@pytest -qq tests
