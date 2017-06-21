#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/warandpeace.html"
html = urlopen(url)

bsObj = BeautifulSoup(html, "html.parser")

"""
findAll(tag, attributes, recursive, text, limit, keywords)
find(tag, attributes, recursive, text, keywords)
    tag -- pass a string name of a tag or even a Python list of string tag names
    attributes -- takes a Python dictionary of attributes and matches tags that contain any one of those attributes
    recursive -- argument is a boolean.
        if true: The findAll function looks into children,and children's children
        if false: it will look only at the top-level tags in your document.
        By default, findAll works recursively
    text -- it matches based on the text content of the tags, rather than properties of the tags themselves
    limit -- is only used in the findAll methods
    keyword -- the keyword argument allows you to select tags that contain a particular attribute.

"""
# bsObj.findAll(tagName, tagAttributes)
nameList = bsObj.findAll("span", {"class": "red"})
for name in nameList:
    print(name.get_text()) # in order to separate the content from the tags

headList = bsObj.findAll({"h1","h2"})
for head in headList:
    print(head.get_text())

print("------------------------------")

bothList = bsObj.findAll("span", {"class":"green", "class":"red"})
for both in bothList:
    print(both.get_text())
print("------------------------------")

timesList = bsObj.findAll(text="the prince")
print(len(timesList))
print("------------------------------")

allText = bsObj.findAll(id="text")
print(allText[0].get_text())
print("------------------------------")

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)
print("------------------------------")
for child in bsObj.find("table",{"id":"giftList"}).descendants:
    print(child)

print("------------------------------")
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
print("------------------------------")
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

"""
BeautifulSoup and regular expressions go hand in hand when it comes to scraping the Web

The solution is to look for something identifying about the tag itself.In this case, we can look at the file path of the product images:
"""

