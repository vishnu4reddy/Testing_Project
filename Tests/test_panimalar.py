# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# print("Starting on the earth")


# def test_panimalar():
#     capabilities = {
#         # "browserName": "chrome",
#         # "browserVersion": "100.0",
#         # "selenoid:options": {
#         #     "enableVideo": False,
#         #     "enableVNC":True,
#         "browserName": "firefox",
#         "browserVersion": "77.0",
#         "selenoid:options": {
#             "enableVideo": False,
#             "enableVNC": True

#         }
#     }
#     driver = webdriver.Remote(
#         command_executor="http://localhost:4444/wd/hub",
#         desired_capabilities=capabilities)
#     driver.maximize_window()
#     driver.get("https://www.google.com/")
#     title = driver.title
#     print(title)
#     assert title == "Google"
#     driver.find_element(By.NAME, "q").send_keys(
#         "panimalar engineering college")
#     driver.find_element(
#         By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").send_keys(Keys.ENTER)
#     driver.find_element(
#         By.XPATH, "//h3[normalize-space()='Panimalar Engineering College']").click()
#     driver.find_element(
#         By.XPATH, "//a[@href='#!'][normalize-space()='Courses']").click()
#     driver.find_element(
#         By.XPATH, "//div[@class='menu-head']//li//a[@href='be-mechanical-engineering.php'][contains(text(),'B.E – Mechanical Engineering')]").click()
#     driver.find_element(
#         By.XPATH, "//body/div[@class='kode-wrapper']/header[@id='mainheader']/div[@class='kode-topbar']/div[@class='container']/div[@class='row']/div[@class='col-md-2']/a[1]").click()
#     driver.close()
#     print("landed on the moon ")
#     # print(dir(driver))


