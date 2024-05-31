import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

radiobtn = driver.find_elements(By.XPATH,"//input[@type='radio']")
print(len(radiobtn))

for radio in radiobtn:
    if radio.get_attribute("value") == "radio2":
        radio.click()
        assert radio.is_selected()
        break

# we can do in different way as bellow
# radiobtn = driver.find_elements(By.XPATH,"//input[@type='radio']")
# radiobtn[2].click()
# assert  radiobtn[2].is_selected()


assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert driver.find_element(By.ID,"hide-textbox").is_displayed()

time.sleep(2)


