import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from programs_fanshawe.items import ProgramsFanshaweItem

class ProgramsFanshawe 