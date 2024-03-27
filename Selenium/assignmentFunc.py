import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(2)
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)
expected_list = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
Product_names = driver.find_elements(By.XPATH,"//div[@class='products']/div/h4")
Actual_list = []
for product_name in Product_names:
    #Actual_list = l.append(product_name.text)
    print(product_name.text)
    Actual_list.append(product_name.text)

print(Actual_list)
assert  expected_list == Actual_list


time.sleep(10)
