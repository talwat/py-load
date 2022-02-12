from setuptools import setup

# Read the contents of the README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='py-load-lib',
    description="A super simple, compact, and easy to use loading bar module for python with no dependencies.",
    version='0.5',
    license='MIT',
    author="Talwat",
    author_email='talwat321@gmail.com',
    py_modules=["py_load"],
    python_requires='>=3.6, <4',
    keywords='loading, bar, loadingbar, loading bar',
    url='https://github.com/talwat/py-load',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
