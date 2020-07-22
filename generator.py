import requests
from bs4 import BeautifulSoup
import random
import pprint
import re


def get_top(index):
    res = requests.get('https://www.gutenberg.org/browse/scores/top')
    soup = BeautifulSoup(res.text, "html.parser")
    regex = re.compile(r"(ebooks\/[0-9]+\"\>)")
    top = regex.findall(str(soup.ol))
    book_num = re.compile(r"([0-9]+)")
    books = book_num.findall(str(top))
    return books[index]


def cut_up_poem():
    try:
        index = get_top(random.randint(1, 101))
        pg = requests.get(f'https://www.gutenberg.org/files/{index}/{index}-h/{index}-h.htm')
        soup2 = BeautifulSoup(pg.text, "html.parser")
        limit = len(soup2.text)-20000
        poem = ''

        def linefunc():
            line = ''
            for i in range(1, 3):
                snick = random.randint(1000, int(limit))
                snippet = soup2.text[int(snick): int(snick)+40]
                linebit = ''.join(s for s in snippet if 31 < ord(s) < 126)
                line += linebit+'||'
            return line

        for item in range(1, 6):
            poem += linefunc()+'\n'
        return poem
    except ValueError:
        print('Ruh-roh. Your scissors missed the page! Try again.')

print(cut_up_poem())



