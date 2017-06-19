#!/usr/bin/env python3
"""
Web scraping using BS4(Beautiful Soup) and requests
Using requests grab a target page
Using BeautifulSoup to parse this raw HTML data
Create a utilities directory
"""
from bs4 import BeautifulSoup # extract the HTML content also parse XML
import requests # a simple yet powerful python HTTP library

def url_open(url):
    """
    Extract raw_html data using requests and
    return the nicely formatted BeautifulSoup object
    for the given url
    """
    try:
        resp = requests.get(url)
        data = BeautifulSoup(resp)
    except Exception as e:
        print(e)
    else:
        return data

if __name__ == '__main__':
    url = 'http://www.reuters.com/places/china'
    url_open(url)

