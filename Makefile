format:
	uv run ruff format .
	uv run ruff check --fix
dev:
	uv run uvicorn app.main:app --reload
db-generate:
	uv run alembic revision --autogenerate -m "Add Note model"
db-migrate:
	uv run alembic upgrade head