"""Config file for pytest fixtures and hooks."""

from pytest import fixture, mark
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from helpers import URL
from datetime import datetime


@fixture
def driver(request, browser):
    if browser.lower() == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--headless")  # remove this if you want to see the browser running
        driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(),
            options=firefox_options
        )
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  # remove this if you want to see the browser running
        driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            chrome_options=chrome_options
        )
    driver.get(URL)
    request.instance.driver = driver

    yield driver
    driver.close()


@fixture
def browser(request):
    return request.config.getoption('-B')


@mark.hookwrapper
def pytest_runtest_makereport(item, call):
    """
    Extends the PyTest Plugin to take and embed screenshots in html report, whenever test fails.
    :param item:
    """
    timestamp = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = f"{timestamp}.png"
            if item.funcargs.get('driver'):
                item.funcargs['driver'].get_screenshot_as_file(f'screenshots/{file_name}')
                if file_name:
                    html = f'<div><img src="screenshots/{file_name}" alt="screenshot" ' \
                           f'style="width:304px;height:228px;" onclick="window.open(this.src)" align="right"/></div>'
                    extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_addoption(parser):
    parser.addoption("-B", "--browser",
                     dest="browser",
                     action="store",
                     default='Chrome',
                     help="Browser. Valid options are chrome and firefox")
