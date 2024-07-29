Topic = "Use the NewsAPI and the requests module to fetch the daily news related to different topics"
print(Topic.center(50))

#https://newsapi.org/
# Key: https://newsapi.org/v2/everything?q=tesla&from=2024-06-13&sortBy=publishedAt&apiKey=25e8d136e1a14804b58f92c43d6e182e

import requests
import json
query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-06-13&sortBy=publishedAt&apiKey=25e8d136e1a14804b58f92c43d6e182e"

r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))

for article in news["articles"]: # dict
    print(article["title"])
    print(article["description"])
    print("--------------------------------------")