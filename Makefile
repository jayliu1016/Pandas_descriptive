install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

test:
	python -m pytest --cov=main test_main.py

generate:
	python test_main.py
	git config --local user.email "action@github.com"
	git config --local user.name "GitHub Action"
	# Only add and commit if there are changes
	git diff-index --quiet HEAD || (git add . && git commit -m "test" && git push) || true

all: install format lint test
