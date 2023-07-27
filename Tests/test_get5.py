# import requests
# import pytest


# @pytest.mark.xfail
# def test_get():
#     resp = requests.get("https://reqres.in/api/unknown/2")
#     json_response = resp.json()
#     print(json_response["data"]["name"])
#     assert (json_response["data"]["id"]) == 2
#     print(json_response["support"]["text"])
#     assert (json_response["support"]["text"]).startswith("To")


# import subprocess

# # Define the command to run
# command = "pytest --markers"

# # Run the command and capture the output
# output = subprocess.check_output(command, shell=True)

# # Decode the output into a string
# output_str = output.decode("utf-8")

# # Filter out the built-in markers
# custom_markers = [line.strip() for line in output_str.split(
#     "\n") if line.startswith("@pytest")]

# # Print the custom markers
# print("\n".join(custom_markers))
