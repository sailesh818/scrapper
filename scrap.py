
# go to git bash
# git config --global user.name "sailesh818"
# git config --global user.email "sailesh7019@gmail.com"

# git init
# git status => if you want to check what are the status of files
# git diff => if you want to check what are the changes 
# git add .
# git commit -m "Your messages"
# copy paste git code from github


#########
# 1. change the code 
# 2. git add.
# 3. git commit -m "Your message"
# 4. git push
###########

import json
import csv
import requests

from bs4 import BeautifulSoup 


url = "http://books.toscrape.com"

def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to load page")
        return []
    
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    
    
    
    book_list = []
    for book in books:
        title = book.h3.a['title']
        print(title)
        price_text = book.find('p', class_='price_color').text
        currency = price_text[0]
        price = float(price_text[1:])
        book_list.append({
            "title": title,
            "currency": currency,
            "price": price
        })
    return book_list

all_books = scrape_books(url)



with open("books.json", "w") as f:
    json.dump(all_books, f, indent= 4, ensure_ascii=False)
    


with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "currency", "price"])
    writer.writeheader()
    writer.writerows(all_books)
