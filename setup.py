import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nomics-python",
    version="2.0.0",
    author="Taylor Facen",
    author_email="taylor.facen@gmail.com",
    description="A python wrapper for the Nomics API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TaylorFacen/nomics-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)