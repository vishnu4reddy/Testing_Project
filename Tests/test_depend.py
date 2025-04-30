# import pytest
# @pytest.mark.dependency()
# @pytest.mark.xfail(reason="deliberate fail")
# def test_a():
#     pass
#     assert True
# @pytest.mark.dependency()
# def test_b():
#     pass
# @pytest.mark.dependency(depends=["test_a"])
# def test_c():
#     pass
# @pytest.mark.dependency(depends=["test_b"])
# def test_d():
#     pass
# @pytest.mark.dependency(depends=["test_b", "test_c"])
# def test_e():
#     pass
import pytest

def test_a():
    assert False

def test_b():
    pass

def test_c():
    pass

def test_d():
    pass


def test_e():
    pass
