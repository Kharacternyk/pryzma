debug: black flake
	@python -q

black:
	@black pryzma/* 2>&1 | tail -n1

flake:
	@flake8 pryzma/*
