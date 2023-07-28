import pytest


@pytest.fixture(params=[1, 2, 3])
def setup_teardown_param(request):
    data = request.param
    # Setup actions based on the data
    yield data
    # Teardown actions


def test_fixture_param(setup_teardown_param):
    # The test will run three times, once for each parameter (1, 2, and 3)
    assert setup_teardown_param > 0
