install:
	pip install -r requirements.txt

test:
	pytest -v

check:
	ruff check

format:
	ruff format
