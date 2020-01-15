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
*   `tests` - test files
*   `drivers` - place your webdrivers here 
    *   [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/)
    *   [geckdodriver](https://github.com/mozilla/geckodriver/releases)
*   `screenshots` - test failure screenshots

## Reporting with screenshots
```py
pytest --html report.html
```

## Rules
*     Standard fare is £2
*     People under 16 travel at half price
*     People 60 or over travel free
*     Anyone travelling off-peak receives a 25% discount
*     Peak travel is from 7.30am up to and including 5.30pm
*     The date of travel must be tomorrow or after
