from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")

titles = soup.find_all(name="h3", class_="title")

movies = []

for title in titles:
    movies.append(title.getText())

movies.reverse()

df = pd.DataFrame(movies, columns=["Movie Title"])
df.to_csv("movies.txt", index=False, header=False)
