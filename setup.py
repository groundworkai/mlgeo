import setuptools
import mlgeo

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mlgeo",
    version=mlgeo.__version__,
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
    python_requires='>=3.7',
    install_requires=[
        'numpy>=1.19',
        'pickle5',
        'pandas'
    ]
)
