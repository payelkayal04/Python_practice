import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys("secret_sauce")
driver.find_element(By.CLASS_NAME, "submit-button").click()
items = driver.find_elements(By.CLASS_NAME,"inventory_item_description ")
itemCarts = driver.find_elements(By.XPATH,"//button[text()='Add to cart']")


for item in items:
    #print(item.text)
    if "T-Shirt" in item.text:
        print(item.text)
        #driver.find_element(By.XPATH,"//button[text()='Add to cart']").click()




time.sleep(15)