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
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")

count = len(products)
print(count)
assert count > 0

for product in products:
    product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

# Price validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)
TotalPrice = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == TotalPrice

#Discounted price validation
AfterDiscountPrice = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert AfterDiscountPrice <= TotalPrice

# driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
# dropdown = Select(driver.find_element(By.XPATH,"//select"))
# dropdown.select_by_value("India")
# driver.find_element(By.CLASS_NAME,"chkAgree").click()
# driver.find_element(By.XPATH,"//button[text()='Proceed']").click()

time.sleep(10)
