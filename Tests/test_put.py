import pytest
# import requests
# payload = {
#     "name": "morpheus",
#     "job": "zion resident"
# }

# @pytest.mark.xfail
# def test_testpost():
#     resp = requests.post("https://reqres.in/api/users/2", data=payload)
#     # data = json.loads(open("data.json","r").read()))
#     print(resp)
#     print(resp.json())
#     assert resp.json()['job'] == 'zion resident'



@pytest.mark.requirements(names="CARE-3206")


def test_version2_fail():
    pass

