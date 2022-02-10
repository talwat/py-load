#!/bin/env bash

rm -r dist
rm -r ./*.egg-info
python3 setup.py sdist
python3 -m pip install twine
twine upload dist/*