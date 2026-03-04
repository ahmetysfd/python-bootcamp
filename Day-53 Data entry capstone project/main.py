import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# --------------------------------------------------
# STEP 1: SCRAPE DATA FROM ZILLOW CLONE
# --------------------------------------------------

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

response = requests.get(ZILLOW_URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "html.parser")

addresses = []
prices = []
links = []

# Each property is inside an <li>
listings = soup.select("ul li")

for listing in listings:
    a_tag = listing.find("a", href=True)
    price_tag = listing.find("span")

    if not a_tag or not price_tag:
        continue

    address = a_tag.get_text(strip=True)
    link = a_tag["href"]
    price = price_tag.get_text(strip=True)

    if "zillow.com" not in link:
        continue

    addresses.append(address)
    prices.append(price)
    links.append(link)

print(f"Scraped {len(addresses)} listings")

# --------------------------------------------------
# STEP 2: SELENIUM – FILL GOOGLE FORM
# --------------------------------------------------

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfEdsR-iJVgxcL_CMwyNDiKaentua_3mXlr8qn_qexHHL4-PA/viewform?usp=header"

service = Service()
driver = webdriver.Chrome(service=service)

for address, price, link in zip(addresses, prices, links):
    driver.get(FORM_URL)
    time.sleep(3)

    # Google Forms text inputs (order matters)
    inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")

    # Question 1: Address
    inputs[0].send_keys(address)

    # Question 2: Price
    inputs[1].send_keys(price)

    # Question 3: Link
    inputs[2].send_keys(link)

    time.sleep(1)

    # Submit form
    submit_button = driver.find_element(By.CSS_SELECTOR, "div[role='button']")
    submit_button.click()

    time.sleep(3)

driver.quit()

print("✅ All listings submitted successfully!")
