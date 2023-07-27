import logging
import os


def setup_function(function):
    logging.info("setting up", function)


def test_func1():
    assert True


def test_func2():
    assert True
