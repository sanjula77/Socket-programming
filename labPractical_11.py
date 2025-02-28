import requests
from bs4 import BeautifulSoup
import csv

def scrape_books():
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    books = []
    page = 1

    while True:
        url = base_url.format(page)
        response = requests.get(url)

        if response.status_code != 200:
            break  # Stop when there are no more pages

        soup = BeautifulSoup(response.text, 'html.parser')
        book_list = soup.find_all('article', class_='product_pod')

        if not book_list:
            break  # Stop if no books are found on the page

        for book in book_list:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.strip()
            availability = book.find("p", class_="instock availability").text.strip()
            books.append([title, price, availability])

        page += 1

    return books

def save_to_csv(books, filename="books.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Availability"])
        writer.writerows(books)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    books_data = scrape_books()
    save_to_csv(books_data)
