# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProgramsFanshaweItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # items requested from midterm pdf 
    progra_name = scrapy.Field()
    program_code = scrapy.Field()
    academic_school = scrapy.Field()
    program_coordinator = scrapy.Field()
    duration = scrapy.Field()

    pass
