from .models import Article
import os
import signal
import sys

from .models import Article
from .paper import get_articles

def startup_hook():
    print("Clearing DB old")
    Article.objects.all().delete() 
    print("Gathering articles")
    articles = get_articles()
    
    for title in articles:
        a = Article(title = title, body=articles[title]["content"],link=articles[title]["url"])
        a.save()

    print("Startup Hook")

def run_startup():
    ## Server Startup Scipt
    startup_hook()
