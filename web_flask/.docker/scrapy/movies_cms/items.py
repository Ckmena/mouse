# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesCmsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    image = scrapy.Field()
    year = scrapy.Field()
    story = scrapy.Field()
<<<<<<< HEAD
=======
    ## Implement the image ??
>>>>>>> ed9496ec1e9ce0fefed0130b68d501b860798112
    pass
