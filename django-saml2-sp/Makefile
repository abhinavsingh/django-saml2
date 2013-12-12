.PHONY: all clean package release

all: clean

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

package:
	python setup.py sdist

release:
	python setup.py sdist register upload
