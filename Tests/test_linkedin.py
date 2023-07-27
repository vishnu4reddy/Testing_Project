# from selenium import webdriver  
# import time 
# from selenium.webdriver.common.by import By 
# from selenium.webdriver.common.keys import Keys
# print("Starting on the earth") 
# def test_linkedin():
#     user_name = "8247548679"
#     password = "vishnu161999"
#     assert password == "vishnu161999"
#     capabilities = {
#     "browserName": "firefox",
#     "browserVersion": "77.0",
#     "selenoid:options": {
#         "enableVideo": False,
#         "enableVNC":True
#     }
#     }
#     driver = webdriver.Remote(
#     command_executor="http://localhost:4444/wd/hub",
#     desired_capabilities=capabilities)
#     driver.maximize_window()  
#     driver.get("https://www.google.com/")  
#     driver.find_element(By.NAME,"q").send_keys("linkedin login") 
#     driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").send_keys(Keys.ENTER)
#     driver.find_element(By.XPATH,"//h3[normalize-space()='LinkedIn Login, Sign in']").click() 
#     driver.find_element(By.NAME,"session_key").send_keys(user_name)  
#     driver.find_element(By.NAME,"session_password").send_keys(password)
#     assert password == "vishnu161999"  
#     driver.find_element(By.XPATH,"//button[@aria-label='Sign in']").click()
#     driver.find_element(By.ID,"ember19").click()
#     driver.find_element(By.ID,"ember20").click()
#     driver.save_screenshot('screenshots.png')
#     # driver.close()  
#     print("landed on the moon,enjoy the space ") 

# test_linkedin()  