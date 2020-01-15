"""Configurations for actions required for interacting with web elements."""

from selenium.webdriver.support.ui import Select
from pytest import mark
from logging import getLogger
from helpers import *

logger = getLogger(__name__)
logger.setLevel("INFO")


@mark.usefixtures("driver")
class Config:

    def select_value(self, selector: str, value: str) -> None:
        """Select value from a drop-down menu"""
        element = Select(self.driver.find_element_by_name(eval(selector)))
        element.select_by_value(value)

        return

    def input_year(self, selector: str, value: str) -> None:
        """Input 4 digits number into a text field"""
        element = self.driver.find_element_by_name(eval(selector))
        element.clear()
        element.send_keys(value)

        return

    def select_time_of_travel(self, hour: str, minute: str) -> None:
        """Select hour and minute for time of travel"""
        self.select_value(travel_time_hour, hour)
        self.select_value(travel_time_minute, minute)

        return

    def select_date(self, date_type: str, day: str, month: str, year: str) -> None:
        """Select day, month, year date for either travel date or birth date"""
        self.select_value(f'{date_type}_date_day', day.lstrip('0'))
        self.select_value(f'{date_type}_date_month', month.lstrip('0'))
        self.input_year(f'{date_type}_date_year', year)

        return

    def calculate_price(self) -> None:
        """Press Calculate button in order to submit the form"""
        self.driver.find_element_by_css_selector(submit_btn).click()

        return

    def get_ticket_price(self) -> str:
        """Read ticket fare from element"""
        ticket_price = self.driver.find_element_by_css_selector(ticket_fare).text

        return ticket_price.strip('£')

    def error_message_on_submit(self, field_name: str) -> str:
        """Get error message on submission"""
        error_message_selector = f'#field_{field_name} > {error_message}'
        return self.driver.find_element_by_css_selector(error_message_selector).text
