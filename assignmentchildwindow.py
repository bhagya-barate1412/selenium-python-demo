from telnetlib import EC

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.util import wait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/#")
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
windowsOpened= driver.window_handles
driver.switch_to.window(windowsOpened[1])
message = driver.find_element(By.CSS_SELECTOR, ".red").text
var = message.split("at")[1].strip().split(" ")[0]
driver.close()
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID,"username").send_keys(var)
driver.find_element(By.ID,"password").send_keys(var)
# wait = WebDriverWait(driver,20)
# wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
# print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
try:
    # Wait for the alert to be visible with a longer timeout
    alert = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
    # Print the alert message
    print(alert.text)
except TimeoutException:
    print("Alert message not found within the specified timeout period.")
