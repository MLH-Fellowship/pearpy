PYTHON=python
POETRY=poetry

test: 
	$(PYTHON) -m test.test_pear

benchmark:
	${PYTHON} -m test.benchmark

install:
	$(POETRY) install
