SHELL := /bin/bash

setup: env-setup

remove: env-remove

precommit: black test

env-setup:
	conda env update -f environment.yml
	source activate fitter-happier && python -m ipykernel install --user --name fitter-happier

env-remove:
	conda env remove -n fitter-happier -y
