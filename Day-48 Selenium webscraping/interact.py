import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name_input = driver.find_element(By.NAME, "fName")
last_name_input = driver.find_element(By.NAME, "lName")
email_input = driver.find_element(By.NAME, "email")
element = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-block")


first_name_input.clear()
first_name_input.send_keys("Ahmet")
last_name_input.send_keys("Demirel")
email_input.send_keys("FDSAFSDA@gmail.com")
element.click()


time.sleep(5)
driver.quit()