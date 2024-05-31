from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#driver.switch_to.frame(driver.find_element(By.ID,"courses-iframe"))
driver.switch_to.frame(driver.find_element(By.XPATH,"/html/body/div[5]/fieldset/iframe"))
# driver.find_element(By.CLASS_NAME,"theme-btn register-btn").click()
driver.implicitly_wait(10)
# driver.switch_to.default_content()
driver.find_element(By.XPATH,"/html/body/div/header/div[2]/div/div/div[2]/div[1]/a").click()
# element.click()

# print(driver.find_element(By.LINK_TEXT," contact@rahulshettyacademy.com").text)
# driver.find_element(By.CLASS_NAME, "theme-btn.register-btn").click()

