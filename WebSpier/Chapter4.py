#!/usr//bin/env python3
#-*- coding: utf-8 -*-
#===========================================
#
#           FILE: Chapter4.py
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
APIs are designed to serve as a lingua franca between different pieces of software that need to share information with each other.

In an example later in this chapter, we will look at combining Wikipedia edit histories (which conatin IP address) with an IP address resolver API in order to get the geographic location of WiKipedia edits around the world.

The Fact that APIs present their data as JSON or XML, rather than HTML

    http://freegeoip.net -- This API resolves IP addresses to geographic locations

There are four ways to request information from a web server via HTTP:
    GET -- When you visit a website through the address bar in your browser.{Used for retrieving resources}
    POST -- When you fill out a form, or submit information, presumably to a backend script on the server.{Used for creating resources}
    PUT -- When interacting with websites, but is used from time to time in APIs.A PUT request is used to update an object or information.{Used for changing/replacing resources or collections}
    DELETE -- It is used to delete an object.{Used for deleting resources}

Authentication:
    Modern APIs require some type of authetication before thet can be used.

http://patorjk.com/

The most common types of response formatting are eXtensible Markup Language (XML) and JavaScript Object Notation (JSON)
    First, JSON files are generally smaller than well-designed XML files.

Spotify Developer -- Web API User Guide
    The base address of the API is https://api.spotify.com
    All requests to the Spotify Web API require authorization and the request header sent by the application must include a valid access token.
    The Spotify Web API is based on REST principles:
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

