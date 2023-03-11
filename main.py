from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")
movies = soup.find_all(name="h3", class_="title")
movies_list = []
with open("movies.text", "w", encoding="utf-8") as file:
    for movie in movies[::-1]:
        file.write(f"{movie.getText()}\n")

# with open("movies.text", "w") as file:
#     for movie in movies_list:
#         file.write(f"{movie}\n")