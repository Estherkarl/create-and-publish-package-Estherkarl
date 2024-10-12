import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="calculations",
    version="0.0.1",
    author= "Estherkarl",
    description="Package for basic mathematical calculations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Estherkarl/calculations",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
