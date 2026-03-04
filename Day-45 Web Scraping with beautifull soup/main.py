from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
titles = soup.find_all("span", class_="titleline")

for title in titles:
    print(title.getText())
