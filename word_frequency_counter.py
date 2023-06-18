import requests
from bs4 import BeautifulSoup
import operator

total_word_count = 0
def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('p'):
        content = post_text.text
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)

    global total_word_count
    total_word_count = len(word_list)

    clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbol = "!@#$%^&*()_+{}[]|:L=-';,./?><:|\"1234567890"
        for i in range(0, len(symbol)):
            word = word.replace(symbol[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    global total_word_count
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        percentage = value * 100 / total_word_count
        print(key, value, percentage)

start('https://en.wikipedia.org/wiki/Antoni_Gaudí')