
from selenium import webdriver

from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsOpened= driver.window_handles
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.implicitly_wait(2)

# driver.get("https://www.w3schools.com/html/default.asp")
#
# driver.find_element(By.LINK_TEXT,"Try it Yourself »").click()
# WindowsOpened =driver.window_handles
# driver.switch_to.window(WindowsOpened[1])

driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == windowsOpened[0]


