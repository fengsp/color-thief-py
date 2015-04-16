clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lines:
	find . -name "*.py"|xargs cat|wc -l

release:
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel upload
