install:
	python -m pip install --upgrade pip
	python -m pip install --upgrade poetry
	poetry install

lock:
	poetry lock --no-update

update:
	poetry update

format:
	poetry run black sandbox
	poetry run ruff --fix sandbox

lint:
	poetry run black --check sandbox
	poetry run ruff check sandbox
	poetry run mypy sandbox

amend:
	git commit --amend --no-edit -a

test:
	poetry run pytest sandbox \
		--last-failed \
		--cov
