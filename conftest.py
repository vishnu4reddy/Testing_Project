# import logging
# import os

# # Set up the logs folder if it doesn't exist
# logs_folder = "logs"
# os.makedirs(logs_folder, exist_ok=True)

# # Configure the logging format
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     handlers=[
#         logging.StreamHandler(),  # Print logs to the console
#         logging.FileHandler(os.path.join(logs_folder, "app.log"))  # Save logs to the log file
#     ]
# )

import pytest

@pytest.fixture
def supply_AA_BB_CC():
    return ['AA', 'BB', 'CC']
