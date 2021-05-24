import pandas as pd
import requests
from bs4 import BeautifulSoup

WEBSITE = "https://quotes.toscrape.com"
html_content = requests.get(WEBSITE).content

soup = BeautifulSoup(html_content, features = "html.parser")

quotes = soup.find_all("div", class_ = "quote")
list_items = [quote.text.strip() for quote in quotes]

cat_quotes = []


for item in list_items:
    cat_quotes.append(item)
    

df = pd.DataFrame({
    'category_name' : cat_quotes
})

df.head()

df.to_csv("quotes_data.csv")

