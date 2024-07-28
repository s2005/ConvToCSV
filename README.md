# ConvToCSV

## Description

ConvToCSV is a Python project designed to streamline the process of converting delimited files to CSV format. It provides a simple and robust solution for handling various input scenarios, including different header formats, multi-line headers, and custom delimiters. This tool is particularly useful for data analysts, researchers, and developers who frequently work with data copied from web pages or exported from various sources and need a reliable way to standardize their data into CSV format.

Key features of ConvToCSV include:

- Automatic detection of header types (delimited or CSV)
- Support for multi-line headers
- Handling of empty lines and fields with spaces
- Customizable encoding options
- Configurable input delimiter
- Command-line interface for easy integration into data processing pipelines
- Debug mode for detailed conversion process information

Whether you're dealing with exported database tables, legacy data formats, or simply need to convert between delimited file types, ConvToCSV offers a straightforward and efficient solution.

## Project Structure

```shell
ConvToCSV/
│
├── .devcontainer/
│   └── devcontainer.json
├── src/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .gitignore
├── .dockerignore
├── requirements.txt
├── setup.py
└── README.md
```

- `.devcontainer/`: Configuration for development container
- `src/`: Contains the main source code of the project
- `tests/`: Contains unit tests
- `.gitignore`: Specifies intentionally untracked files to ignore
- `.dockerignore`: Specifies files and directories that should be excluded when building a Docker image
- `requirements.txt`: List of Python dependencies
- `setup.py`: Package setup file
- `README.md`: This file

## Development Container

This project uses a development container to ensure a consistent development environment across different machines. The devcontainer includes:

- Python 3.11
- zsh shell with Oh My Zsh
- pytest for running unit tests
- Common Python development tools and libraries

To use the devcontainer:

1. Ensure you have Docker and Visual Studio Code with the "Remote - Containers" extension installed.
2. Open the project folder in VS Code.
3. When prompted, click "Reopen in Container", or run the "Remote-Containers: Reopen in Container" command from the Command Palette.

The devcontainer will automatically set up the development environment with all necessary dependencies.

## Requirements

- Python 3.11 or higher

This package has been tested only with Python 3.11. Compatibility with other versions is not guaranteed.

## Installation

If you're not using the devcontainer, you can set up the project environment manually:

1. Clone the repository:

   ```shell
   git clone https://github.com/yourusername/ConvToCSV.git
   cd ConvToCSV
   ```

2. Create a virtual environment (optional but recommended):

   ```shell
   python -m venv venv
   source venv/bin/activate
   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Install the package in editable mode (optional):

   ```shell
   pip install -e .
   ```

   **Note: After installing with `pip install -e .`, the `convtocsv` command becomes available system-wide, allowing you to run it from any directory.**

5. Install the package in editable mode with the dev dependencies (optional):

   ```shell
   pip install -e .[dev]
   ```

## Usage

Here's a basic example of how to use ConvToCSV:

### As a Python module

```python
from src.main import convert_tab_to_csv

# Convert a tab-delimited file to CSV
convert_tab_to_csv('input.txt', 'output.csv', encoding='utf-8', header_lines=2, delimiter='\t')

# Convert a pipe-delimited file to CSV
convert_tab_to_csv('input.txt', 'output.csv', encoding='utf-8', header_lines=2, delimiter='|')
```

### For command-line usage

```shell
# For tab-delimited input
python src/main.py input.txt output.csv --encoding utf-8 --header-lines 2 --delimiter '\t'

# For pipe-delimited input (see note on escaping below)
python src/main.py input.txt output.csv --encoding utf-8 --header-lines 2 --delimiter '|'
```

To enable debug mode and see detailed information about the conversion process:

```shell
python src/main.py input.txt output.csv --encoding utf-8 --header-lines 2 --delimiter '\t' --debug
```

### As a command-line tool when installed in editable mode

```shell
conv2csv input.txt output.csv
```

### Note on Delimiters

When using special characters like the pipe (|) as delimiters in command-line arguments, it's important to properly escape or quote them to prevent the shell from interpreting them as special operators. Here are the recommended ways to use the pipe character as a delimiter:

1. Escaping with a backslash:

   ```shell
   python src/main.py input.txt output.csv --delimiter \|
   ```

2. Using single quotes (preferred method):

   ```shell
   python src/main.py input.txt output.csv --delimiter '|'
   ```

3. Using double quotes:

   ```shell
   python src/main.py input.txt output.csv --delimiter "|"
   ```

Single quotes are generally preferred for literal strings in shell scripts because they prevent any interpretation of the contents. Double quotes allow for some interpretation (like variable expansion), but will still treat the pipe as a literal character.

Command-line arguments:

- `input_file`: Path to the input delimited file
- `output_file`: Path to the output CSV file
- `--encoding`: File encoding (default: utf-8)
- `--header-lines`: Number of header lines (default: 1)
- `--delimiter`: Input file delimiter (default: '\t')
- `--debug`: Enable debug output (optional)

The `--delimiter` option allows you to specify the character used to separate fields in the input file. For tab-delimited files, use `--delimiter '\t'`. For pipe-delimited files, use `--delimiter '|'` (with proper escaping as shown above).

## Running Tests

To run the tests for this project:

```shell
python -m pytest tests/
```

To run the tests if you have installed the package in editable mode with the dev dependencies:

```shell
pytest tests/
```

## Contributing

Contributions to ConvToCSV are welcome! Here's how you can contribute:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please note that when you open a pull request, **GitHub Actions will automatically run our test suite. This automated testing occurs only on pull requests, not on every commit.** Ensure that all tests pass before submitting your pull request. If you've added new functionality, please include appropriate tests.

To check if your changes pass the tests locally before submitting a pull request, run:

```shell
python -m pytest tests/
```

This will help streamline the review process and increase the chances of your contribution being accepted quickly.
