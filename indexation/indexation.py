import urllib.robotparser
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import numpy
from urllib.parse import urlsplit
import requests
from nltk.tokenize import word_tokenize
from nltk import FreqDist
from collections import defaultdict
import json
from statistics import mean

def import_json_to_list(json_file_path):
    f = open(json_file_path)
    return json.load(f)

def extract_title(url_page : str):
    try:
        response = urllib.request.urlopen(url_page, timeout=1.0).read().decode('utf-8')
        page = BeautifulSoup(response, 'html.parser')
        title = page.title.get_text()
    except Exception as e:
        title = ''
    print(url_page)
    return title

def tokenize(string):
    return word_tokenize(string)

def tokenize_list(list_string : list):
    list_token = []
    for string in list_string:
        list_token.append(word_tokenize(string.lower()))
    return list_token

def word_frequency(tokens : list):
    frequence = FreqDist(tokens)
    return frequence

def create_inverted_index(list_token):
    index = defaultdict(list)
    for i, tokens in enumerate(list_token):
        frequence = dict(word_frequency(tokens))
        for token in tokens:
            count = frequence[token]
            index[token].append(f"{i}:{count}")
    for k,v in index.items():
        index[k] = [*set(v)]
    return index

def create_stats(list_token):
    number_of_docs = len(list_token)
    number_of_tokens = sum(len(l) for l in list_token)
    mean_per_doc = mean([len(l) for l in list_token])
    my_dict = {'number_of_docs' : number_of_docs, 'number_of_tokens' : number_of_tokens, 'mean_per_doc' : mean_per_doc}
    return my_dict

def export_dict(dict: dict, file_name : str):
    data_json = json.dumps(dict, indent=3)
    with open(file_name, "w", encoding='utf8') as f1:
        f1.write(data_json)