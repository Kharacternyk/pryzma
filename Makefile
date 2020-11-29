debug: black flake shell

shell:
	@python -i pryzma.py

black:
	@black pryzma.py 2>&1 | tail -n1

flake:
	@flake8 pryzma.py
