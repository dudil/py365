import setuptools

VERSION = '0.0.4'

CLASSIFIERS = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py365",
    version=VERSION,
    author="Dudi Levy",
    author_email="dudil@users.noreply.github.com",
    description="Python Library for App Development over MS Open Graph ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dudil/py365",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    classifiers=CLASSIFIERS,
)
