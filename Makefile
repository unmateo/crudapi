include .env
.DEFAULT_GOAL := help
help:
	make --help
install:
	poetry install
lint:
	poetry run black .
test:
	poetry run pytest --cov=crudapi --cov-report=xml tests/
publish:
	poetry publish --build --username __token__ --password $(PYPI_TOKEN)
