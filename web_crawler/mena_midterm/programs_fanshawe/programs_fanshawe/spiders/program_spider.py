import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from programs_fanshawe.items import ProgramsFanshaweItem

class ProgramsFanshawe(CrawlSpider):
    name = 'program'
    allowed_domains = ['fanshawec.ca']
    start_urls = [
        'https://www.fanshawec.ca/programs/'
    ]

    rules = (
        Rule(LinkExtractor(allow=('programs',)), callback='parse_item'),
    )

    def parse_item(self, response):
        program_item = ProgramsFanshaweItem()
        program_item['program_name'] = response.css('.title::text').get().strip()
        program_item['program_code'] = response.css('.views-field-field-program-code div::text').get().strip()
        program_item['academic_school'] = response.css('.field-name-field-academic-school a::text').get().strip()
        program_item['program_coordinator'] = response.css('.field-name-field-program-coordinator p::text').get().strip()
        # program_item['duration'] = response.css('p::text')[1].get().strip()
        yield program_item
        
        # https://www.fanshawec.ca/programs/
        #https://www.fanshawec.ca/programs-and-courses?field_area%5B%5D=148 
        #https://www.fanshawec.ca/programs/idp3-interactive-media-design/next