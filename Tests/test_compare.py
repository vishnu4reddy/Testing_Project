import pytest


@pytest.mark.xfail
@pytest.mark.another_custom_marker
def test_greater():
    num = 100
    assert num > 100


@pytest.mark.xfail
@pytest.mark.greatest_of_all_time
def test_greater_equal():
    num = 100
    assert num >= 100


@pytest.mark.skip
@pytest.mark.custom_poraraiii
def test_less():
    num = 100
    assert num < 200
