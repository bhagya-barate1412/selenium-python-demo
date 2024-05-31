import time

from selenium import webdriver
from selenium.webdriver.common.by import By

expectedList = ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actualList = []
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(results)
assert count>0
for result in results:
    actualList.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click()

assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.implicitly_wait(3)

driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")

#driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/button").click()

prices=driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum=0
for price in prices:
    sum=sum+int(price.text)

print(sum)

totalAmount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum == totalAmount


discount=float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert totalAmount >= discount