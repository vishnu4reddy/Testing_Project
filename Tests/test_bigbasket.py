# from selenium import webdriver  
# import time 
# from selenium.webdriver.common.by import By 
# from selenium.webdriver.common.keys import Keys
# number = "9490058514"
# print("Starting on the earth")
# def test_bigbasket():
#     capabilities = {
#     "browserName": "chrome",
#     "browserVersion": "100.0",
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
#     driver.find_element(By.NAME,"q").send_keys("bigbasket") 
#     driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").send_keys(Keys.ENTER)
#     driver.find_element(By.XPATH,"//h3[normalize-space()='BigBasket']").click()
#     driver.find_element(By.XPATH,"//a[@ng-show='vm.newLoginFlow']").click()
#     driver.find_element(By.XPATH,"//input[@id='otpEmail']").send_keys(number)
#     driver.find_element(By.XPATH,"//button[@type='submit'][normalize-space()='Continue']").click()
#     time.sleep(3)
#     driver.find_element(By.XPATH,"//button[normalize-space()='Verify & Continue']").click()
#     time.sleep(15)
#     driver.find_element(By.XPATH,"//a[@class='btn hvr-fade']//span[@class='new-caret']").click()
#     driver.find_element(By.XPATH,"//a[@ng-click='vm.logout()']").click()
#     driver.close()  
#     print("landed on the moon ")


# test_bigbasket()