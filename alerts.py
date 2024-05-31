import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name="Bhagya"
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert=driver.switch_to.alert
alertText =alert.text
print(alertText)
assert name in alertText

#alert.dismiss()

alert.accept()


time.sleep(2)
