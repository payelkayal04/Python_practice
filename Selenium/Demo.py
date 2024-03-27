#Implicit wait
#Explicit Wait
#Pause the test for few seconds using time class
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise")
#driver.implicitly_wait(5)
# wait untill 5 seconds if object is not displayed
#Global wait
#1.5 second to reach next page - execution will resume in 1.5 seconds

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,"input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements(By.XPATH,"//div[@class='products']/div"))
assert count == 3


