import requests, bs4
from bs4 import BeautifulSoup


def youtube_search(username):
    url = "https://youtube.com/@{}".format(username)
    r = requests.get(url)
    page = r.content
    features = "html.parser"
    soup = BeautifulSoup(page, features)