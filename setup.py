import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name = "nomics-python",
    version = "3.0.2",
    author = "Taylor Facen",
    author_email = "taylor.facen@gmail.com",
    description = "A python wrapper for the Nomics API",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/TaylorFacen/nomics-python",
    packages = setuptools.find_packages(),
    install_requires = required,
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)