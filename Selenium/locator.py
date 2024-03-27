import time

from pymongo.max_staleness_selectors import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.NAME, "name").send_keys("Payel")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()

# // Xpath -->> //tagname[@attribute='value'] -> //input[@attribute = 'submit']
# // CSS selector -->> tagname[attribute='value'] -> input[attribute = 'submit'] , #id, .classname
driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
driver.find_element(By.CSS_SELECTOR, "input[id='inlineRadio2']").click()
# driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("Payel")
#Static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
#dropdown.select_by_visible_text("Female")
#dropdown.select_by_value()


message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys(" Hello Again")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()

time.sleep(5)
