install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games ||:

push-dev:
	git merge dev
	git push origin
	git switch dev

format:
	poetry run black -l 79 brain_games

black-diff:
	poetry run black -l 79 --diff brain_games