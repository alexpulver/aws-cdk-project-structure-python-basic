#!/bin/bash

set -o errexit
set -o verbose

targets=(api app.py constants.py deployment.py)

bandit --recursive "${targets[@]}"
black --check --diff "${targets[@]}"
flake8 --config .flake8 "${targets[@]}"
isort --settings-path .isort.cfg --check --diff "${targets[@]}"
# mypy: split commands due to https://github.com/python/mypy/issues/4008
mypy --config-file .mypy.ini "${targets[@]:0:1}"
mypy --config-file .mypy.ini "${targets[@]:1}"
pylint --rcfile .pylintrc "${targets[@]}"
safety check -r api/runtime/requirements.txt -r requirements.txt -r requirements-dev.txt
# Report code complexity
radon mi "${targets[@]}"
# Exit with non-zero status if code complexity exceeds thresholds
xenon --max-absolute A --max-modules A --max-average A "${targets[@]}"
