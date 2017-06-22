#!/usr//bin/env python3
#-*- coding: utf-8 -*-
#===========================================
#
#           FILE: Chapter4-ParsingJSON.py
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
http://freegeoip.net/json/50.78.253.58
which resolves IP addresses to physical addresses
"""

import json # The JSON parsing library used is part of Python's core library
from urllib.request import urlopen

def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response) # return JSON objects into dictionaries
    return responseJson.get("country_code")

print(getCountry("50.78.253.58"))

"""
How python JSON library handles the different values that might be encountered in a JSON string
"""
jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],"arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'
jsonObj = json.loads(jsonString)

print(jsonObj.get("arrayOfNums"))
print(jsonObj.get("arrayOfNums")[1])
print(jsonObj.get("arrayOfNums")[1].get("number")+jsonObj.get("arrayOfNums")[2].get("number"))
print(jsonObj.get("arrayOfFruits")[2].get("fruit"))

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

