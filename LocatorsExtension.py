import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("allenadam@gmail.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Bhagya@123")
driver.find_element(By.ID, "confirmPassword").send_keys("Bhagya@123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# driver.find_element(By.ID, "userEmail").send_keys("allenadam@gmail.com")
# driver.find_element(By.ID, "userPassword").send_keys("Pass#123")
# driver.find_element(By.XPATH, "//input[@type='submit']").click()


time.sleep(5)



