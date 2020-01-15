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

## Bugs

[PROJ-BUG-1]() Minimize window and notice elements dissapear although they are clickable ([screenshot](https://imgur.com/JSVnl2L)).

[PROJ-BUG-2]() There are two options with value = 31 in dropdowns ([screenshot](https://imgur.com/ZHje32x)).

[PROJ-BUG-3]() Link in footer has a typo in it (mercry instead of mercury - [screenshot](https://imgur.com/AKycPea)).

[PROJ-BUG-4]() Standard fare for 15 years old people, born in 2004 ([screenshot](https://imgur.com/2VG7FTt))

[PROJ-BUG-5]() Standard fare for 14 years old people, born in 2005 ([screenshot](https://imgur.com/nBhKRvd))

[PROJ-BUG-6]() No fare for 59 years old people, born in 1960 ([screenshot](https://imgur.com/EcBTSEF))

[PROJ-BUG-7]() Standard fare for 60 years old people, born in 1960 ([screenshot](https://imgur.com/vdfy9Bd))
