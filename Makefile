

clean-build:
	rm -fr build/
	rm -fr htmlcov/
	rm -fr .tox/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +


clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

test: clean-pyc
	python -B -R -tt -W ignore setup.py test

dist: test clean-build clean-pyc
	pip install wheel
	python setup.py sdist bdist_wheel

check: dist
	pip install check-manifest pyroma restview
	check-manifest
	pyroma .
	restview --long-description
