import pandas as pd
import requests
from bs4 import BeautifulSoup

WEBSITE = "https://quotes.toscrape.com"
html_content = requests.get(WEBSITE).content

soup = BeautifulSoup(html_content, features = "html.parser")

names = soup.find_all("small", class_ = "author")
author_name = [name.text.strip() for name in names]

quotes = soup.find_all("span", class_ = "text")
list_items = [quote.text.strip() for quote in quotes]

tags = soup.find_all("meta", class_ = "keywords")


cat_names = []
cat_quotes = []
cat_tags = []


for i in range(len(list_items)):
    cat_quotes.append(list_items[i])
    cat_names.append(author_name[i])
    
for tag in tags:
    cat_tags.append(tag['content'])

    

df = pd.DataFrame({
    'Name of the author' : cat_names ,
    'Quote' : cat_quotes ,
    'Tags' : cat_tags
})

df.head()

df.to_csv("quotes_data.csv")

