#!/usr//bin/env python3
#-*- coding: utf-8 -*-
#===========================================
#
#           FILE: WebScrap.py
#
#           USAGE:
#
#   DESCRIPTION:
#
#       OPTIONS: ----
#  REQUIREMENTS: ----
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
Scraping Rules
    1. You should check a website's Terms and Conditions before you scrape it.Be careful to read the statements about legal use of data.Usually, the data you scrape should not be used for commercial purposes.
    2. Do not request data from the website too aggressively with you program (also known as spamming), as this may break the website. Make sure your program behaves in a reasonable manner(i.e. acts like a human).One request for one webpage per second is good practice,
    3. The layout of a website may change from time to time, so make sure to revisit the site and rewrite your code as needed.
Inspecting the Page:
    https://www.apple.com/shop/buy-iphone/iphone-7
    First, right-click and open your browser's inspector to inspect the webpage.
    Second, We can see that the price is inside a few levels of HTML tags

<div class="column large-6 small-6 first">
    <div class="as-dimension-wrapper">
        <div class="as-dimension-pricebox">
            <div class="price-point price-point-fullPrice">
                <span class="nowrap">$649</span>
"""

# import libraries
import urllib.request
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.apple.com/shop/buy-iphone/iphone-7'

# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(quote_page)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
price = soup.find('span', attrs={'class': 'nowrap'})

prices = price.text.strip() # strip() is used to remove starting and trailing
print(prices)
