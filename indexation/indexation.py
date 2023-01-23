import urllib.robotparser
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import numpy
from urllib.parse import urlsplit
import requests
from nltk.tokenize import word_tokenize

def extract_title(url_page : str):
    try:
        response = urllib.request.urlopen(url_page)
        page = BeautifulSoup(response)
        title = page.title.get_text()
    except Exception as e:
        title = ''
    return title

def tokenize(string):
    return word_tokenize(string)

def tokenize_list(list_string : list):
    list_token = []
    for string in list_string:
        list_token.append(word_tokenize(string))
    return list_token

