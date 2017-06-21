#!/usr//bin/env python3
#-*- coding: utf-8 -*-
#===========================================
#
#           FILE: Chapther3.py
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
Web crawlers are called such beacuse they crawl across the Web.

Write a Python that retrieves an arbitrary Wikipedia page and produces a list of Links on that page:
"""

from urllib.request import urlopen
from urllib.error import *
from bs4 import BeautifulSoup
import re
import datetime
import random

"""
Random number generator seed with the current system time
Most random number algorithms strive to produce an evently distributed and hard-to-predict sequence of numbers
The Python pseudorandom number generator is powered by the Mersenne Twister algorithm
"""
random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    try:
        html = urlopen("http://en.wikipedia.org"+articleUrl)
    except HTTPError as e:
        return None  # return nil, break, or do some other "Plan B"
    else:
        bsObj = BeautifulSoup(html, "html.parser")

        return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")

while len(links) > 0:
    newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)


#########################################################
#  _____ _           ___   __          _                #
# /  __ \ |         (_) \ / /         (_)               #
# | /  \/ |__  _   _ _ \ V /__ _  __ _ _ _ __   __      #
# | |   | '_ \| | | | | \ // _` |/ _` | | '_ \ / _` |   #
# | \__/\ | | | |_| | | | | (_| | (_| | | | | | (_| |   #
#  \____/_| |_|\__, |_| \_/\__,_|\__, |_|_| |_|\__, |   #
#               __/ |               | |         __/ |   #
#              |___/                |_|        |___/    #
#########################################################

