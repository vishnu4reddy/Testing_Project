# import smtplib
# from email.mime.text import MIMEText

# # Email configuration
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# sender_email = 'vishnuvardhanuv36@gmail.com'
# recipient_email = 'vishnuvardhanuv36@gmail.com'
# subject = 'Test Email'
# message = 'This is a test email sent via SMTP.'

# # Create a MIMEText object with the email content
# msg = MIMEText(message)
# msg['Subject'] = subject
# msg['From'] = sender_email
# msg['To'] = recipient_email

# # Connect to Gmail's SMTP server and send the email
# try:
#     with smtplib.SMTP(smtp_server, smtp_port) as server:
#         server.starttls()  # Enable TLS encryption
#         server.login(sender_email, 'vishnu16REDDY@')
#         server.send_message(msg)
#         print("Email sent successfully!")
# except Exception as e:
#     print(f"Error sending email: {e}")
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.select import Select
# from bomb.imp import mail, pasword, first_name, last_name
email = "yamini6349@gmail.com"
password = "Yaminimudigeti2@"
firstname = "Mudigeti"
phonenumber = "9390989026"
Lastname = "Yamini"

# def Bdaychock():
print("Start")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.1800baskets.com/?entryBrand=berries")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//button[@id='truste-consent-button']").click()
time.sleep(5)
# al = driver.switch_to.alert
# al.dismiss()
# # driver.find_element(By.XPATH,"//div[@id='signInDropdown']").click()
# driver.find_element(By.XPATH,"//img[@id='hp-sign-in']").click()
# driver.find_element(By.XPATH,"//a[@id='click-here-dropdown']").click()
menubutton = driver.find_element(By.XPATH, "//img[@id='hp-sign-in']")
achains = ActionChains(driver)
achains.move_to_element(menubutton).click().perform()
driver.find_element(By.XPATH, "//a[@id='click-here-dropdown']").click()
time.sleep(5)
win = driver.window_handles
driver.switch_to.window(win[1])
driver.maximize_window()
driver.find_element(By.ID, "firstNameField").send_keys(firstname)
driver.find_element(
    By.XPATH, "//input[@id='lastNameField']").send_keys(Lastname)
driver.find_element(By.ID, "emailField").send_keys(email)
# time.sleep(5)
driver.find_element(
    By.XPATH, "//input[@id='passwordField-ca']").send_keys(password)
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='emailOptInField']").click()
driver.find_element(By.ID, "createAccBtn").click()
time.sleep(5)
driver.find_element(
    By.XPATH, "//div[@id='createAccErr']//a[contains(text(),'Sign In')]").click()
time.sleep(5)
driver.find_element(By.ID, "emailField-signIn").send_keys(email)
driver.find_element(
    By.XPATH, "//input[@id='passwordField-signIn']").send_keys(password)
driver.find_element(By.ID, "signInBtn").click()
time.sleep(5)
driver.switch_to.window(win[0])

# al = driver.switch_to.alert
# al.dismiss()
time.sleep(5)
driver.find_element(By.ID, "Birthday▸_2").click()
time.sleep(5)
driver.execute_script("window.scrollTo(0, 300)")
driver.find_element(By.XPATH, "//input[@value='recipient|him']").click()
time.sleep(5)
driver.execute_script("window.scrollTo(0, 2000)")
time.sleep(5)

driver.find_element(
    By.XPATH, "//img[@alt='Magical Unicorn Truffle Cake Pops']").click()
time.sleep(5)
driver.find_element(By.ID, "product-sku 1009-174943S").click()
# driver.execute_script("window.scrollTo(0, 300)")
time.sleep(5)
driver.execute_script("window.scrollTo(0, 1000)")
driver.find_element(
    By.XPATH, "//span[normalize-space()='Write A Review']").click()
driver.find_element(By.XPATH, "//span[@aria-label='score 4']").click()
driver.find_element(By.NAME, "review_title").send_keys("Good")
driver.find_element(By.NAME, "review_content").send_keys(
    "So fun and cute, everything arrived perfectly too! Thank you!")
time.sleep(2)
driver.find_element(By.NAME, "display_name").send_keys("Yamini")
time.sleep(3)
driver.find_element(By.NAME, "email").send_keys(email)
time.sleep(3)
driver.find_element(By.XPATH, "//input[@aria-disabled='false']").click()

time.sleep(5)
driver.close()
print("end")
