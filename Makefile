include .env
export $(shell sed 's/=.*//' .env)
.DEFAULT_GOAL := help
help:
	make --help
install:
	poetry install
update:
	poetry update
lint:
	poetry run black .
test:
	poetry run pytest --cov=crudapi --cov-report=xml tests/
publish:
	poetry publish --build --username __token__ --password $(PYPI_TOKEN)
