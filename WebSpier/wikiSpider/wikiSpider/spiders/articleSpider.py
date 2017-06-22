#!/usr//bin/env python3
#-*- coding: utf-8 -*-
#===========================================
#
#           FILE: articleSpider.py
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

from scrapy.spiders import CrawlSpider, Rule
from wikiSpider.items import Article
from scrapy.linkextractors import LinkExtractor

class ArticleSpider(CrawlSpider):
    name = "article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Main_Page","http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
    rules = [Rule(LinkExtractor(allow=('(/wiki/)((?!:).)*$'),), callback="parse_item", follow=True)]

    def parse_item(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is: "+title)
        item['title'] = title
        return item


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

