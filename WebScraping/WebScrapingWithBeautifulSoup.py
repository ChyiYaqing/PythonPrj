#!/usr//bin/env python3
#-*- coding: utf-8 -*-
#===========================================
#
#           FILE: WebScrapingWithBeautifulSoup.py
#
#           USAGE:
#
#   DESCRIPTION: "Web scrapting(Web harvesting or web data extraction) is a computer software technique of extracting information from websites."
#               HTML parsing is easy in Python, especially with help of the BeautifulSoup library.
#
#       OPTIONS: ----
#  REQUIREMENTS: ---- Using Beautiful Soup 4 and Requests {pip install beautifulsoup4, pip install requests}
#          BUGS: ----
#         NOTES: ----
#        AUTHOR: Chyi Yaqing
#  ORGANIZATION:
#       VERSION: 0.1.0
#       CREATED: 04/24/2017
#      REVISION: ----
#      Copyright © 2017 Chyi Yaqing
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software FOundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAB PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#===================================================================

"""
Beautiful Soup provides a few simple methods and Pythonic idioms for navigating searching,and modifying a parse tree: a toolkit for dissecting a document and extracting what you need.
Beaufitul Soup automatically convert incoming documents to Unicode and outgoing documents to UTF-8
Beautiful Soup sits on the top of popular Python parsers like lxml and html5lib.
"""

# Extracting URL's from any website
from bs4 import BeautifulSoup
import requests

url = input("Enter a website to extract the URL's from: ")
r = requests.get("http://" + url)
data = r.text
soup = BeautifulSoup(data)
for link in soup.find_all('a'):
    print(link.get('href'))


