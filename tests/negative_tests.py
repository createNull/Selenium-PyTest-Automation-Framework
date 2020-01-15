"""Negative scenarios for validating input fields and drop-down menus"""

from config import *


class NegativeTests(Config):

    def test_field_is_required(self):
        logger.info("Verify all fields are required on submit")

        self.calculate_price()
        assert self.error_message_on_submit("travel_time") == err_req_field
        assert self.error_message_on_submit("travel_date") == err_req_field
        assert self.error_message_on_submit("date_of_birth") == err_req_field

    @mark.parametrize("day,month,year,expected_error", [("31", "2", "7777", err_invalid_date),
                                                        ("10", "12", "#2%x", err_invalid_date),
                                                        ("31", "2", "100", err_invalid_date)])
    def test_field_has_valid_date(self, day, month, year, expected_error):
        logger.info("Verify date is valid")
        self.select_date("travel", day, month, year)
        self.select_date("birth", day, month, year)

        self.calculate_price()
        assert self.error_message_on_submit("travel_date") == expected_error
        assert self.error_message_on_submit("date_of_birth") == expected_error

    @mark.parametrize("age_category,expected_error", [("young", err_earliest_day),
                                                     ("adult", err_earliest_day),
                                                     ("elder", err_earliest_day)])
    def test_earliest_travel_day_is_tomorrow(self, age_category, expected_error):
        logger.info("Verify earliest travel day is tomorrow")

        self.select_time_of_travel("20", "00")

        day_of_travel, month_of_travel, year_of_travel = days_from_now(days=0).split(' ')
        self.select_date('travel', day_of_travel, month_of_travel, year_of_travel)

        day_of_birth, month_of_birth, year_of_birth = random_birth_date(category=age_category).split(' ')
        self.select_date('birth', day_of_birth, month_of_birth, year_of_birth)

        self.calculate_price()
        assert self.error_message_on_submit("travel_date") == expected_error

    def test_future_birth_date(self):
        logger.info("Birth date can't be in the future")

        self.select_date('birth', "15", "4", "8888")

        self.calculate_price()
        assert self.error_message_on_submit("date_of_birth") == err_future_birth_day
