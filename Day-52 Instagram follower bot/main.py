from selenium import webdriver
from selenium.webdriver.ie.service import Service

SIMILAR_ACCOUNT = "nuggets"
password = "789632145Aa"
email = "sadfad781@gmail.com"

class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

        service = Service()
        self.driver = webdriver.Chrome()

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):

        pass


bot = InstaFollower
bot.login()
bot.find_followers()
bot.follow()