import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)
products = driver.find_elements(By.XPATH,"//div[@class='products']/div")

count = len(products)
print(count)
assert count > 0

for product in products:
    product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR,".cart-icon").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
#time.sleep(2)
driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
#time.sleep(5)
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
dropdown = Select(driver.find_element(By.XPATH,"//select"))
dropdown.select_by_value("India")
driver.find_element(By.CLASS_NAME,"chkAgree").click()
driver.find_element(By.XPATH,"//button[text()='Proceed']").click()

time.sleep(5)