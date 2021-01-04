import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mlgeo",
    version="0.0.1",
    author="Nick Machairas",
    author_email="nick@groundwork.ai",
    description="Repository for Machine Learning in Geotechnics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/groundworkai/mlgeo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
