PYTHON=python
POETRY=poetry

test:
	$(PYTHON) -m tests.test_pear

benchmark:
	${PYTHON} -m tests.benchmark

install:
	$(POETRY) install --no-interaction

publish:
	make install
	$(PYTHON) setup.py sdist
	twine upload --skip-existing dist/*
