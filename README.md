# Selenium BDD Framework

A robust Behavior-Driven Development (BDD) framework for web automation testing using Selenium WebDriver, Python, and pytest-bdd.

## 🚀 Features

- BDD approach using Gherkin syntax
- Selenium WebDriver integration
- Parallel test execution support
- Allure reporting
- Excel data handling
- Configurable test environment
- Page Object Model implementation

## 📋 Prerequisites

- Python 3.13
- Chrome WebDriver (compatible with your Chrome browser version)
- pip (Python package installer)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirment.txt
```

## 🏗️ Project Structure

```
Python_BDD_Framwork/
├── config/             # Configuration files
├── project/           # Test implementation
│   ├── features/      # Gherkin feature files
│   ├── pages/         # Page Object Models
│   └── stepDefinitions/ # Step definitions
├── reports/           # Test execution reports
├── TestData/          # Test data files
├── utils/             # Utility functions
├── SupportFiles/      # Supporting files
└── conftest.py        # Pytest configuration
```

## 🧪 Running Tests

### Using Tox
```bash
tox
```

### Using pytest directly
```bash
pytest
```

### Running with Allure Report
```bash
pytest --alluredir=./reports
allure serve ./reports
```

## 🔧 Configuration

- Environment configurations can be modified in the `config` directory
- Test data can be updated in the `TestData` directory
- Browser settings can be adjusted in `conftest.py`

## 📊 Reports

The framework generates Allure reports for test execution. To view the reports:

1. After test execution, generate the report:
```bash
allure generate ./reports
```

2. Open the report:
```bash
allure open
```

## 🛠️ Dependencies

- selenium: Web automation
- pytest-bdd: BDD implementation
- allure-pytest: Test reporting
- openpyxl: Excel file handling
- pytest-xdist: Parallel test execution
- toml: Configuration file handling
- requests: HTTP requests

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details. 