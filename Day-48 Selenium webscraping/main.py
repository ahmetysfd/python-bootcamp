from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://g8hh.github.io/cookieclicker/")

wait = WebDriverWait(driver, 10)

try:
    # Wait for overlay to appear
    wait.until(EC.visibility_of_element_located((By.ID, "darken")))

    # Try to find and click the close button inside the overlay if exists
    close_button = driver.find_element(By.CSS_SELECTOR, "#darken .close, #darken button")  # adjust selector as needed
    close_button.click()

    # Wait until overlay disappears
    wait.until(EC.invisibility_of_element_located((By.ID, "darken")))
except:
    # If no overlay or no close button, ignore and continue
    pass

try:
    while True:
        wait.until(EC.invisibility_of_element_located((By.ID, "darken")))
        cookie = driver.find_element(By.ID, "bigCookie")
        cookie.click()
except KeyboardInterrupt:
    print("Stopped clicking")
