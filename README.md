# Selenium-PyTest-Automation-Framework

## Prerequisites:
*   Python 3.x

## Browsers supported
*   Google Chrome
*   Mozilla Firefox

## Local setup & installation:
*   Create and activate [virtual environment](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments)
*   Install project requirements using pip
```
pip install -r requirements.txt
```
*   Execution
```py
# Run all tests
pytest

# Run one test
pytest tests/acceptance_tests.py::AcceptanceTests::test_fare_for_adult

# Run all tests in parallel
pytest -vs -nauto
```
## Directories
*   `drivers` - place your webdrivers here 
    *   [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/)
    *   [geckdodriver](https://github.com/mozilla/geckodriver/releases)
*   `screenshots` - test failure screenshots
*   `tests` - test cases

## Reporting and screenshots
```py
pytest --html report.html
```
