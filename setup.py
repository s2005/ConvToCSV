from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ConvToCSV",
    version="0.1.0",
    description="A tool to convert plan text file with fields to CSV format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11"
    ],
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "convtocsv=main:main",
        ],
    },
    install_requires=[
        # The project currently doesn't have any runtime dependencies.
        # If you add any in the future, list them here.
    ],
    extras_require={
        'dev': [
            'pytest',
            'pylint',
        ],
    },
)