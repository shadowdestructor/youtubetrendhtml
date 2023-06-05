import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get
        ('https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl').content, 'html.parser')

#take all html codes
print(soup.find_all("html"))