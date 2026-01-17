from bs4 import BeautifulSoup
import requests

url = "https://www.w3.org/TR/html52/"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')
title = soup.title.string

print(f"Page Title: {title}")