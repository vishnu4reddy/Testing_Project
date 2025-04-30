#
import pytest
import allure

@allure.feature("Search")
@allure.story("Search by keyword")
def test_search_by_keyword():
    assert "python" in "pytest with python"

@allure.feature("Cart")
@allure.story("Add item to cart")
def test_add_to_cart():
    assert True
