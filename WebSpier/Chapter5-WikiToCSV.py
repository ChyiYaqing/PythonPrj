#!/usr//bin/env python3
#-*- coding: utf-8 -*-
#===========================================
#
#           FILE: Chapter5-WikiToCSV.py
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
http://en.wikipedia.org/wiki/Comparison_of_text_editors
Wikipedia's Comparison of Text Editors provides a fairly complex HTML table,complete with color coding, links sorting, and other HTML garbage that needs to be discarded before it can be written to CSV

"""
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "html.parser")

# The main comparson table is currently the first table on the page
table = bsObj.findAll("table",{"class":"wikitable"})[0]
rows = table.findAll("tr")

csvFile = open("./files/editors.csv", 'wt')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
    for cell in row.findAll(['td','th']):
        csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()



########################################################
#   _____ _   _ _    _    ___      _                   #
#  / ____| \ | | |  | |  / / |    (_)                  #
# | |  __|  \| | |  | | / /| |     _ _ __  _   ___  __ #
# | | |_ | . ` | |  | |/ / | |    | | '_ \| | | \ \/ / #
# | |__| | |\  | |__| / /  | |____| | | | | |_| |>  <  #
#  \_____|_| \_|\____/_/   |______|_|_| |_|\__,_/_/\_\ #
########################################################


#######################################################################################################################
#  ,----..    ,---,                                                                                                   #
# /   /   \ ,--.' |               ,--,                   ,---,              ,----.     ,--,                           #
#|   :     :|  |  :             ,--.'|                  /_ ./|             /   /  \-.,--.'|         ,---,             #
#.   |  ;. /:  :  :             |  |,             ,---, |  ' :            |   :    :||  |,      ,-+-. /  |  ,----._,. #
#.   ; /--` :  |  |,--.     .--,`--'_            /___/ \.  : |   ,--.--.  |   | .\  .`--'_     ,--.'|'   | /   /  ' / #
#;   | ;    |  :  '   |   /_ ./|,' ,'|            .  \  \ ,' '  /       \ .   ; |:  |,' ,'|   |   |  ,"' ||   :     | #
#|   : |    |  |   /' :, ' , ' :'  | |             \  ;  `  ,' .--.  .-. |'   .  \  |'  | |   |   | /  | ||   | .\  . #
#.   | '___ '  :  | | /___/ \: ||  | :              \  \    '   \__\/: . . \   `.   ||  | :   |   | |  | |.   ; ';  | #
#'   ; : .'||  |  ' | :.  \  ' |'  : |__             '  \   |   ," .--.; |  `--'""| |'  : |__ |   | |  |/ '   .   . | #
#'   | '/  :|  :  :_:,' \  ;   :|  | '.'|             \  ;  ;  /  /  ,.  |    |   | ||  | '.'||   | |--'   `---`-'| | #
#|   :    / |  | ,'      \  \  ;;  :    ;              :  \  \;  :   .'   \   |   | :;  :    ;|   |/       .'__/\_: | #
# \   \ .'  `--''         :  \  \  ,   /                \  ' ;|  ,     .-./   `---'.||  ,   / '---'        |   :    : #
#  `---`                   \  ' ;---`-'                  `--`  `--`---'         `---` ---`-'                \   \  /  #
#                           `--`                                                                             `--`-'   #
#######################################################################################################################

