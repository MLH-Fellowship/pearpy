PYTHON=python
POETRY=poetry

test:
	$(PYTHON) -m tests.test_pear

benchmark:
	${PYTHON} -m tests.benchmark

install:
	$(POETRY) install --no-interaction
