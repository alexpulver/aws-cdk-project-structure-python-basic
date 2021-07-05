#!/bin/bash

set -o errexit
set -o verbose

_targets=(api app.py deployment.py)

bandit --recursive "${_targets[@]}"
black --check --diff "${_targets[@]}"
flake8 --config .flake8 "${_targets[@]}"
isort --settings-path .isort.cfg --check --diff "${_targets[@]}"
mypy --config-file .mypy.ini --strict api  # Splitting commands due to https://github.com/python/mypy/issues/4008
mypy --config-file .mypy.ini --strict app.py deployment.py
pylint --rcfile .pylintrc "${_targets[@]}"
safety check -r api/runtime/requirements.txt -r requirements.txt -r requirements-dev.txt