# ConvToCSV

## Description

ConvToCSV is a Python project designed to streamline the process of converting tab-delimited files to CSV format. It provides a simple and robust solution for handling various input scenarios, including different header formats and multi-line headers. This tool is particularly useful for data analysts, researchers, and developers who frequently work with data copied from web pages and need a reliable way to standardize their data into CSV format.

Key features of ConvToCSV include:

- Automatic detection of header types (tab-delimited or CSV)
- Support for multi-line headers
- Handling of empty lines and fields with spaces
- Customizable encoding options
- Command-line interface for easy integration into data processing pipelines
- Debug mode for detailed conversion process information

Whether you're dealing with exported database tables, legacy data formats, or simply need to convert between delimited file types, ConvToCSV offers a straightforward and efficient solution.

## Project Structure

```shell
ConvToCSV/
│
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── src/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .gitignore
├── .dockerignore
├── requirements.txt
└── README.md
```

- `.devcontainer/`: Configuration for development container
- `.devcontainer/Dockerfile`: Docker configuration
- `src/`: Contains the main source code of the project
- `tests/`: Contains unit tests
- `.gitignore`: Specifies intentionally untracked files to ignore
- `.dockerignore`: Specifies files and directories that should be excluded when building a Docker image
- `requirements.txt`: List of Python dependencies
- `README.md`: This file

## Development Container

This project uses a development container to ensure a consistent development environment across different machines. The devcontainer includes:

- Python 3.9
- zsh shell with Oh My Zsh
- pytest for running unit tests
- Common Python development tools and libraries

To use the devcontainer:

1. Ensure you have Docker and Visual Studio Code with the "Remote - Containers" extension installed.
2. Open the project folder in VS Code.
3. When prompted, click "Reopen in Container", or run the "Remote-Containers: Reopen in Container" command from the Command Palette.

The devcontainer will automatically set up the development environment with all necessary dependencies.

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

## Usage

Here's a basic example of how to use ConvToCSV:

```python
from src.main import convert_tab_to_csv

# Convert a tab-delimited file to CSV
convert_tab_to_csv('input.txt', 'output.csv', encoding='utf-8', header_lines=2)
```

For command-line usage:

```shell
python src/main.py input.txt output.csv --encoding utf-8 --header-lines 2
```

To enable debug mode and see detailed information about the conversion process:

```shell
python src/main.py input.txt output.csv --encoding utf-8 --header-lines 2 --debug
```

Command-line arguments:

- `input_file`: Path to the input tab-delimited file
- `output_file`: Path to the output CSV file
- `--encoding`: File encoding (default: utf-8)
- `--header-lines`: Number of header lines (default: 1)
- `--debug`: Enable debug output (optional)

## Running Tests

To run the tests for this project:

```shell
python -m pytest tests/
```

## Contributing

Contributions to ConvToCSV are welcome! Here's how you can contribute:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please note that when you open a pull request, GitHub Actions will automatically run our test suite. This automated testing occurs only on pull requests, not on every commit. Ensure that all tests pass before submitting your pull request. If you've added new functionality, please include appropriate tests.

To check if your changes pass the tests locally before submitting a pull request, run:

```shell
python -m pytest tests/
```

This will help streamline the review process and increase the chances of your contribution being accepted quickly.
