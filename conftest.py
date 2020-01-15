"""Config file for pytest fixtures and hooks."""

from pytest import fixture, mark
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from helpers import URL
from datetime import datetime

chrome_options = ChromeOptions()
chrome_options.add_argument("--headless")  # remove this if you want to see the browser running

firefox_options = FirefoxOptions()
firefox_options.add_argument("--headless")  # remove this if you want to see the browser running


@fixture
def driver(request):
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Firefox(options=firefox_options)  # need to automate this
    driver.get(URL)
    request.instance.driver = driver

    yield driver
    driver.close()


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
