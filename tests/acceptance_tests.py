"""Each test runs for two time periods, one for on-peak period and other for off-peak period.
Travel date can be hardcoded or be generated depending on the current day.
Birth date can be hardcoded or be randomly generated depending on age category or just age"""

from config import *


class AcceptanceTests(Config):

    @mark.parametrize("hour,minute,expected_fare", [("17", "30", "2.00"), ("23", "45", "1.50")])
    def test_fare_for_adult(self, hour, minute, expected_fare):
        logger.info(f"Verify standard fare at {hour}:{minute} is £{expected_fare}")

        self.select_time_of_travel(hour, minute)

        day_of_travel, month_of_travel, year_of_travel = days_from_now(days=2).split(' ')
        self.select_date('travel', day_of_travel, month_of_travel, year_of_travel)

        day_of_birth, month_of_birth, year_of_birth = random_birth_date(category='adult').split(' ')
        self.select_date('birth', day_of_birth, month_of_birth, year_of_birth)

        self.calculate_price()
        assert self.get_ticket_price() == expected_fare

    @mark.parametrize("hour,minute,expected_fare", [("10", "45", "1.00"), ("02", "15", "0.75")])
    def test_fare_for_young(self, hour, minute, expected_fare):
        logger.info(f"Verify fare for young people at {hour}:{minute} is £{expected_fare}")

        self.select_time_of_travel(hour, minute)

        day_of_travel, month_of_travel, year_of_travel = days_from_now(days=1).split(' ')
        self.select_date('travel', day_of_travel, month_of_travel, year_of_travel)

        b_day, b_month, b_year = random_birth_date(category='young').split(' ')
        self.select_date('birth', b_day, b_month, b_year)

        self.calculate_price()
        assert self.get_ticket_price() == expected_fare

    @mark.parametrize("hour,minute,expected_fare", [("15", "15", "0.00"), ("00", "00", "0.00")])
    def test_fare_for_elder(self, hour, minute, expected_fare):
        logger.info(f"Verify fare for people 60 or over at {hour}:{minute} is £{expected_fare}")
        self.select_time_of_travel(hour, minute)

        day_of_travel, month_of_travel, year_of_travel = days_from_now(days=5).split(' ')
        self.select_date('travel', day_of_travel, month_of_travel, year_of_travel)

        b_day, b_month, b_year = random_birth_date(category='elder').split(' ')
        self.select_date('birth', b_day, b_month, b_year)

        self.calculate_price()
        assert self.get_ticket_price() == expected_fare

    # Corner case tests
    @mark.xfail(reason="PROJ-BUG-4, PROJ-BUG-5")
    @mark.parametrize("hour,minute,expected_fare", [("16", "30", "1.00"), ("01", "15", "0.75")])
    def test_fare_for_age_15(self, hour, minute, expected_fare):
        logger.info(f"Verify fare for 15 years old people at {hour}:{minute} is £{expected_fare}")
        self.select_time_of_travel(hour, minute)

        day_of_travel, month_of_travel, year_of_travel = days_from_now(days=1).split(' ')
        self.select_date('travel', day_of_travel, month_of_travel, year_of_travel)

        day_of_birth, month_of_birth, year_of_birth = random_birth_date(age=15).split(' ')
        self.select_date('birth', day_of_birth, month_of_birth, year_of_birth)

        self.calculate_price()
        assert self.get_ticket_price() == expected_fare

    @mark.parametrize("hour,minute,expected_fare", [("07", "30", "2.00"), ("17", "45", "1.50")])
    def test_fare_for_age_16(self, hour, minute, expected_fare):
        logger.info(f"Verify fare for 16 years old people at {hour}:{minute} is £{expected_fare}")
        self.select_time_of_travel(hour, minute)

        day_of_travel, month_of_travel, year_of_travel = days_from_now(days=1).split(' ')
        self.select_date('travel', day_of_travel, month_of_travel, year_of_travel)

        day_of_birth, month_of_birth, year_of_birth = random_birth_date(age=16).split(' ')
        self.select_date('birth', day_of_birth, month_of_birth, year_of_birth)

        self.calculate_price()
        assert self.get_ticket_price() == expected_fare

    @mark.xfail(reason="PROJ-BUG-6, PROJ-BUG-7")
    @mark.parametrize("hour,minute,expected_fare", [("11", "45", "2.00"), ("07", "00", "1.50")])
    def test_fare_for_age_59(self, hour, minute, expected_fare):
        logger.info(f"Verify fare for 59 years old people is £{expected_fare}")
        self.select_time_of_travel(hour, minute)

        day_of_travel, month_of_travel, year_of_travel = days_from_now(days=1).split(' ')
        self.select_date('travel', day_of_travel, month_of_travel, year_of_travel)

        day_of_birth, month_of_birth, year_of_birth = random_birth_date(age=59).split(' ')
        self.select_date('birth', day_of_birth, month_of_birth, year_of_birth)

        self.calculate_price()
        assert self.get_ticket_price() == expected_fare

    @mark.parametrize("hour,minute,expected_fare", [("17", "30", "0.00"), ("07", "15", "0.00")])
    def test_fare_for_age_60(self, hour, minute, expected_fare):
        logger.info(f"Verify fare for 60 years old people is £{expected_fare}")
        self.select_time_of_travel(hour, minute)

        day_of_travel, month_of_travel, year_of_travel = days_from_now(days=1).split(' ')
        self.select_date('travel', day_of_travel, month_of_travel, year_of_travel)

        day_of_birth, month_of_birth, year_of_birth = random_birth_date(age=60).split(' ')
        self.select_date('birth', day_of_birth, month_of_birth, year_of_birth)

        self.calculate_price()
        assert self.get_ticket_price() == expected_fare
