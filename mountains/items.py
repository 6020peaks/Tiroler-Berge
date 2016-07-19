# -*- coding: utf-8 -*-

import scrapy


class MountainItem(scrapy.Item):
    name = scrapy.Field()
    elevation = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    photo = scrapy.Field()
    url = scrapy.Field()
    hasMap = scrapy.Field()

