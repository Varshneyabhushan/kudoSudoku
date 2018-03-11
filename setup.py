from setuptools import setup,find_packages

classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ]




with open ('README.rst') as f:
	long_description = f.read()

setup(
    name = "kudosudoku",
    version = "1.0.7",
    description = "Sudoku solver,that solves sudoku puzzles using constraint programming",
    url = "https://github.com/VarshneyaB/kudoSudoku.git",
    author = "Varshneyabhushan",
    author_email = "varshneyacoder@gmail.com",
    license = "MIT License",
    packages = find_packages(),
    long_description = long_description,
    classifiers = classifiers,
    keywords = "sudoku solving solve puzzle kudos constraint"
)