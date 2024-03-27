import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(2)
driver.maximize_window()

assert "An iFrame containing the TinyMCE WYSIWYG Editor" == driver.find_element(By.TAG_NAME, "h3").text
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")
assert "Your content goes here.I am able to automate frames" == driver.find_element(By.ID, "tinymce").text
driver.switch_to.default_content()


time.sleep(4)