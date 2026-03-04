from selenium import webdriver
from selenium.webdriver.common.by import By
import time


PROMISED_DOWN = 300
PROMISED_UP = 300
X_EMAIL = "saddad0618@gmail.com"
X_PASSWORD = "789632145"

class InternetSpeedTwitterBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)  # keeps Chrome open
        options.add_argument("user-data-dir=C:/Users/Ahmet/AppData/Local/Google/Chrome/User Data")  # your Chrome data folder
        options.add_argument("profile-directory=Default")  # your active Chrome profile folder

        self.driver = webdriver.Chrome(options=options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)

        try:
            accept_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
            accept_button.click()
            print("Accepted cookies.")
        except:
            print("No cookie button found or already accepted.")

        go_button = self.driver.find_element(By.CLASS_NAME, value="start-text")
        go_button.click()

        time.sleep(90)

        up_result = self.up = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        down_result = self.down = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

        print(up_result)
        print(down_result)

    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(5)

        email_box = self.driver.find_element(By.CSS_SELECTOR,
                                             'input[class="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7"]')
        email_box.send_keys(X_EMAIL)
        time.sleep(3)

        next_button = self.driver.find_element(By.CSS_SELECTOR,
                                               'div[class="css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-184id4b r-13qz1uu r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l"]')
        next_button.click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
