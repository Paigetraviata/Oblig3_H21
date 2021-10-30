from leap_year import is_leap_year


def test_years_divisable_by_4_an_not_100_are_leap_years():
    for year in (2004, 2008, 2012, 2016, 2020):
        assert is_leap_year(year) == True

def test_years_divisable_by_100_and_not_400_are_not_leap_years():
    for year in (1700, 1800, 1900):
        assert is_leap_year(year) == False

def test_years_divisable_by_400_are_leap_years():
    for year in (2000, 2400, 1200, 3200):
        assert is_leap_year(year) == True

def test_years_not_divisable_by_4_are_not_leap_years():
    for year in (2100, 2050):
        assert is_leap_year(year) == False
