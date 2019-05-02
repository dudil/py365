import setuptools

VERSION = '0.1.2'

CLASSIFIERS = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent',
    'Development Status :: 3 - Alpha',
]

REQUIRES = [
    'adal >= 1.2.1',
    'requests >= 2.21.0',
    'urllib3 >= 1.24.2',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py365",
    version=VERSION,
    author="Dudi Levy",
    author_email="dudil@users.noreply.github.com",
    description="Python Library for App Development over MS Graph365 ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/dudil/py365",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    classifiers=CLASSIFIERS,
    install_requires=REQUIRES,
)