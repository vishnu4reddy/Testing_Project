import pytest
import logging
import os


@pytest.fixture
def first():
    logging.info("Set up first fixture")
    yield
    logging.info("Clean up first fixture")


@pytest.fixture
def second(first):
    logging.info("Set up second fixture")
    yield
    logging.info("Clean up second fixture")


def test_context_fixture_order(second):
    logging.info("In the test")
    assert True
