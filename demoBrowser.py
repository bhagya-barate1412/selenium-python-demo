import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/")

print(driver.title)
print(driver.current_url)








time.sleep(5)
