import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

radioBtns = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(radioBtns))

for radioBtn in radioBtns:
    if radioBtn.get_attribute("value") == "radio1":
        radioBtn.click()
        assert radioBtn.is_selected()
        break


assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

time.sleep(5)
