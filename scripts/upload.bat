rm -r dist
rm -r *.egg-info
python setup.py sdist || py setup.py sdist
pip install twine
twine upload dist/*