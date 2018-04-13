import pytest
from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert catmath.cat_years_to_hooman_years(8) == 40


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(0.75) == 3.75


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True


@pytest.mark.parametrize('hooman_age, cat_age', [
    (8, 40),
    (0.75, 3.75),
    (0, 0),
])
def test_cat_to_hooman(hooman_age, cat_age):
    assert catmath.cat_years_to_hooman_years(hooman_age) == cat_age
