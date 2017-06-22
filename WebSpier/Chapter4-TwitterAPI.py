#!/usr//bin/env python3
#-*- coding: utf-8 -*-
#===========================================
#
#           FILE: Chapter4-TwitterAPI.py
#
#           USAGE:
#
#   DESCRIPTION: The following code connects to the Twitter API and prints a JSON list of tweets containing the hashtag#python.
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

from twitter import *

AccessToken = '735437057145733120-eri6pEkxk7LRyYaUgOe0lHj8hOcu3al'
AccessTokenSecret = 'BskDnACNhZnC6mny97fi2328AxTZ6Ue2ab872nfdw5RPU'
ConsumerKey = 'TUQDFWLzHiv1lJPvEifU25pvI'
ConsumerSecret = 'iTqwBQLkMPh9caAJ8NpkWoubaxuG8UnaBsq7vzIRaG500lVK9c'

t = Twitter(auth=OAuth(AccessToken,AccessTokenSecret,ConsumerKey,ConsumerSecret))

# This is the result of sending a single tweet.
#statusUpdate = t.statuses.update(status='Hello, world!')
#print(statusUpdate)

#pythonTweets = t.search.tweets(q = "#python")
#print(pythonTweets)

# In this case, we are asking for the last five tweets that were posted to @montypython's timeline
pythonStatuses = t.statuses.user_timeline(screen_name="montypython", count=5)
print(pythonStatuses)

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

