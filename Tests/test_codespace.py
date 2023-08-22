from Libraries.github import LoginPage
from playwright.sync_api import Page
from Data import config
Email = config.user_git
password = config.git_pass


def test_check_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(Email, password)
    login_page.repositories()
    login_page.test_files()
    login_page.Codespaces()

# from selenium import webdriver
# import time
# import pytesseract
# from PIL import Image
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# def read_captcha(image_path):
#     captcha_image = Image.open(image_path)
#     captcha_text = pytesseract.image_to_string(captcha_image)
#     return captcha_text

# print("Start")
# email = "ymudigeti@msystechnologies.com"
# password = "Yaminimudigeti2@"

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.google.com/")
# time.sleep(3)
# dropdown = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
# dropdown.click()
# dropdown.send_keys("keka login")
# dropdown.send_keys(Keys.ENTER)
# time.sleep(4)
# driver.find_element(By.XPATH, "//h3[normalize-space()='Keka Login']").click()
# time.sleep(4)
# driver.find_element(By.XPATH, "//input[@id='email']").send_keys(email)
# time.sleep(5)
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//p[normalize-space()='Keka Password']").click()
# time.sleep(2)

# # Capturing captcha image
# captcha_element = driver.find_element(By.XPATH, "//img[@id='imgCaptcha']")
# captcha_image_src = captcha_element.get_attribute('src')
# driver.get(captcha_image_src)

# # Downloaded captcha image will be saved in the current working directory
# captcha_image_path = "captcha.png"
# time.sleep(2)
# captcha_element.screenshot(captcha_image_path)

# # Use Tesseract OCR to extract the text from the captcha image
# captcha_code = read_captcha(captcha_image_path)

# # Fill the captcha input field with the extracted captcha code
# code_input = driver.find_element(By.XPATH, "//input[@id='captcha']")
# code_input.send_keys(captcha_code)

# time.sleep(4)
# driver.find_element(By.XPATH, "//button[@class='btn btn-primary mt-10 border-0']").click()
# time.sleep(4)
# driver.close()
# print("end")

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import requests
# print("Start")
# email = "ymudigeti@msystechnologies.com"
# password = "Yaminimudigeti2@"

# # Set up the Selenium webdriver
# driver = webdriver.Chrome()

# # Navigate to the page with captcha
# driver.get("https://www.google.com/")
# time.sleep(3)
# dropdown = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
# dropdown.click()
# dropdown.send_keys("keka login")
# dropdown.send_keys(Keys.ENTER)
# time.sleep(4)
# driver.find_element(By.XPATH, "//h3[normalize-space()='Keka Login']").click()
# time.sleep(4)
# driver.find_element(By.XPATH, "//input[@id='email']").send_keys(email)
# time.sleep(5)
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//p[normalize-space()='Keka Password']").click()
# time.sleep(2)


# # Assuming the captcha image is identified by a specific CSS selector
# captcha_img = driver.find_element(By.XPATH, "//img[@id='imgCaptcha']")

# # Get the URL of the captcha image
# captcha_img_url = captcha_img.get_attribute('src')

# # Download the captcha image
# captcha_img_response = requests.get(captcha_img_url, stream=True)
# with open('captcha_image.png', 'wb') as img_file:
#     img_file.write(captcha_img_response.content)

# # Use Ant i-Captcha API to solve the captcha
# anti_captcha_api_key = 'your_anti_captcha_api_key'
# captcha_solver_url = f'http://api.anti-captcha.com/createTask'
# captcha_solver_data = {
#     'clientKey': anti_captcha_api_key,
#     'task': {
#         'type': 'ImageToTextTask',
#         'body': captcha_img_response.content,
#         'phrase': False,
#         'case': False,
#         'numeric': 0,
#         'math': False,
#         'minLength': 0,
#         'maxLength': 0
#     }
# }

# response = requests.post(captcha_solver_url, json=captcha_solver_data)
# task_result = response.json()

# # Get the task ID from the response
# task_id = task_result['taskId']

# # Poll the Anti-Captcha API for captcha solution
# while True:
#     time.sleep(5)
#     solution_response = requests.get(f'http://api.anti-captcha.com/getTaskResult?clientKey={anti_captcha_api_key}&taskId={task_id}')
#     solution_result = solution_response.json()

#     if solution_result['status'] == 'ready':
#         captcha_solution = solution_result['solution']['text']
#         break

# # Enter the captcha solution in the input field
# captcha_input = driver.find_element(By.ID, 'captcha_input')
# captcha_input.send_keys(captcha_solution)

# # Continue with the rest of your automation
# # ...

# # Close the webdriver
# driver.quit()
