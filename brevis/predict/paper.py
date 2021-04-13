import random
import os
import sys

import newspaper

from tools.trie import *

import requests
from bs4 import BeautifulSoup
from newsapi import NewsApiClient

# NUM_POPULAR_URLS = 3
# NUM_EACH_POPULAR = 2
# FORGET_ARTICLE = False

NUM_ARTICLES = 20

BASE_DIR = Path(__file__).resolve().parent.parent
SAVED_TRIE_DIR = BASE_DIR / 'tools' / 'savedtries'

def get_articles():
    newsapi = NewsApiClient(api_key='d84cf1257d084ed3b9eec34250c389ca')

    all_articles_response = newsapi.get_everything(sources='bbc-news,the-verge',
                                        domains='bbc.co.uk,techcrunch.com',
                                        language='en',
                                        sort_by='relevancy')

    title_content_dict = {}
    articles = all_articles_response['articles']

    for i in range(NUM_ARTICLES):
        article = articles[i]
        title = article['title']
        if title in title_content_dict:
            continue

        html = requests.get(article['url'])
        soup = BeautifulSoup(html.text, 'html.parser')

        content = [p_tag.get_text() for p_tag in soup.find_all('p')]
        content = '\n'.join(content)

        title_content_dict[title] = {'content':content,'url':article['url']}

    return title_content_dict



# def forget_articles(url):
#     print(f"Forgettig {url} articles")
#     domain = \
#         url.replace("https://", "http://").replace("http://", "").split("/")[0]
#     d_pth = os.path.join(newspaper.settings.MEMO_DIR, domain + ".txt")
#     if os.path.exists(d_pth):
#         os.remove(d_pth)

# def get_articles():

#     word_checker = Trie()
#     print(SAVED_TRIE_DIR / 'trie.pkl')
#     print("Loading word checker...")
#     word_checker.load(SAVED_TRIE_DIR / 'trie.pkl')

#     print(f"Obtaining {NUM_POPULAR_URLS} popular URLs")
#     populars = newspaper.popular_urls()[:NUM_POPULAR_URLS]

#     for p in populars:
#         if FORGET_ARTICLE:
#             forget_articles(p)
#         print(p)

#     print("Building popular newspapers...")
#     popular_newspaper_build = []
#     for idx, p in enumerate(populars):
#         print(f"Building {idx + 1} \t {p}")
#         popular_newspaper_build.append(newspaper.build(p, memoize_articles = False, language='en'))

#     print("Getting articles text list...")
#     articles_text_list = []
#     title_article_dict = {}

#     for pb in popular_newspaper_build:
#         size = len(pb.articles)
#         print(f"{pb.brand} has {size} articles.")
#         for _ in range(NUM_EACH_POPULAR):
            
#             while True:
#                 index = random.randint(0, size-1)
#                 print(index, end = ' ')
#                 article = pb.articles[index]
#                 try:
#                     article.download()
#                     article.parse()
#                     title = article.title
#                     text = article.text

#                     if not text:
#                         raise Exception('')
#                 except:
#                     continue
                
#                 print(text, word_checker.test_corpus__(text))
#                 title_article_dict[title] = text
#                 # articles_text_list.append(text)
#                 break
#         print()

#     return title_article_dict
