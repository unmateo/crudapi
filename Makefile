.DEFAULT_GOAL := help
help:
	make --help
install:
	poetry install
lint:
	poetry run black .
test:
	dotenv -f "$(pwd)/.env" run poetry run pytest --cov=crudapi --cov-report=xml tests/
