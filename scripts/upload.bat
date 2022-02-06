rm -r dist
rm -r *.egg-info
py setup.py sdist
pip install twine
twine upload dist/*