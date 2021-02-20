build:
	poetry build


install:
	poetry install


package-install:
	pip install --user dist/*.whl


lint:
	poetry run flake8 page_loader


test:
	poetry run python3 -m pytest --cov=page_loader --cov-report xml tests/ -vv


coverage:
	poetry run coverage xml
