"""
Beautiful Soup is a Python library for pulling data out of HTML and XML files.
"""
import urllib.request
from bs4 import BeautifulSoup

# open file to write data
f = open('./university-list.txt','w')
url = "http://www.utexas.edu/world/univ/alpha/"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page,"lxml")
