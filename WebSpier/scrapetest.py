"""
In Python 3.x, urllib2 was renamed urllib and was split into several submodules:
    urllib.request : for opening and reading URLs
    urllib.parse : for parsing URLs
    urllib.error : containing the exceptions raised by urllib.request
    urllib.robotparser : for parsing robots.txt file
"""
from urllib.request import urlopen
from urllib.error import *
# Virtually any information can be extracted from any HTML (or XML) file
from bs4 import BeautifulSoup
"""
There are two main things that can be go wrong in this line:
    The page is not found on the server -- HTTP error "404"
    The server is not found -- Internal Server Error 500 - urlopen returns a None object
    urlopen function will throw the generic exception "HTTPError"
"""
try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
    # return null, break, or do some other "Plan B"
except URLError:
    print("URL is not found")
else:
    # program continues, Note: If you return or break in the
    # exception catch, you do not need to use the "else" statement

    # html.read() in order to get the HTML content of the page
    bsObj = BeautifulSoup(html.read(), "html.parser")
    # BeautifulSoup object structure (html -> body -> h1)

    # If you attempt to access a tag that does not exits.BeautifulSoup will return a None object
    # retun AttributeError
    print(bsObj.h1)
    print(bsObj.body.h1)
    print(bsObj.html.h1)
    print(bsObj.html.body.h1)


    print(bsObj.find("nonExistent"))

    try:
        badContent = bsObj.find("h1")
    except AttributeError as e:
        print("Tag was not found")
    else:
        if badContent == None:
            print("Tag was not found")
        else:
            print(badContent)

url = "http://pythonscraping.com/pages/page1.html"
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle(url)
if title == None:
    print("Title could not be found")
else:
    print(title)
