#!/usr//bin/env python3
#-*- coding: utf-8 -*-
#===========================================
#
#           FILE: Chapter4-IPaddress.py
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
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")

    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    # Format of revision history pages is:
    # http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
    print("history url is: "+historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, "html.parser")

    #finds only the links with class "mw-anonuserlink" which has IP addresses
    # instead of usernames indicating an anonymous user with an IP address, rather than a username and returns it as a set
    ipAddresses = bsObj.findAll("a", {"class":"mw-anouserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_code")

links = getLinks("/wiki/Python_(programming_language)")

while(len(links)) > 0:
    for link in links:
        print("--------------------")
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP+" is from "+country)

    newLink = links[random.randint(0, len(links)-1)].attrs["href"]
    links = getLinks(newLink)


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

