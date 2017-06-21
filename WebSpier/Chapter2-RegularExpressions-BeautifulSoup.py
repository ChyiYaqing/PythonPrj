#!/usr//bin/env python3
#-*- coding: utf-8 -*-
#===========================================
#
#           FILE: Chapter2-RegularExpressions-BeautifulSoup.py
#
#           USAGE:
#
#   DESCRIPTION: The solution is to look for something identifying about the tag itself.In this case,we can look at the file path of the product images
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

from urllib.request import urlopen
from bs4 import BeautifulSoup, re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")

bsObj = BeautifulSoup(html,"html.parser")
# A regular expression can be inserted as any argument in a BeautifulSoup expression, allowing you a great deal of flexibility in finding target elements.
images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})

for image in images:
    print(image["src"])

"""
A lambda expression is a function that is passed into another function as a variable.

"""

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

