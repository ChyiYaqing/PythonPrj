#!/usr//bin/env python3
#-*- coding: utf-8 -*-
#===========================================
#
#           FILE: Chapter5.py
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
Need to be able to save the information that they scrape

Media Files:
    Two main ways to store media files:
        Reference -- Store the URL
        Download
urllib.urlretrieve download files from any remote URL

"""
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os # the is module acts as an interface between Python and the operating syste.

downloadDirectory = "Downloads"
baseUrl = "http://pythonscraping.com"

def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://"+source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("//www."):
        url = "https:"+source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://"+source
    else:
        url = baseUrl+"/"+source
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.", "")
    path = path.replace(baseUrl, "")
    path = downloadDirectory+path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, "html.parser")
downloadList = bsObj.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)

urlretrieve(fileUrl, getDownloadPath(baseUrl,fileUrl,downloadDirectory))

#imageLocation = bsObj.find("a",{"id":"logo"}).find("img")["src"]
#urlretrieve(imageLocation, "logo.jpg")


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

