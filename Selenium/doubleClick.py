import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.context_click(driver.find_element(By.ID ,"double-click")).perform()  #right click

action.double_click(driver.find_element(By.ID,"double-click")).perform()

alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(5)
driver.close()