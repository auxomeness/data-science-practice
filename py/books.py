import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.find("p")["class"][1]

    print(title, price, rating)