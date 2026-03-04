from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

tinder_url = "https://tinder.com/app/recs"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(tinder_url)
wait = WebDriverWait(driver, 15)



log_in = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='Oturum aç']"))
)
log_in.click()

google_login_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="container-div"]/div/div[2]'))
)
google_login_btn.click()


time.sleep(2)  # Give popup time to open
main_window = driver.current_window_handle
for handle in driver.window_handles:
    if handle != main_window:
        driver.switch_to.window(handle)
        break