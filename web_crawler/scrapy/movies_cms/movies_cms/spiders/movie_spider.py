import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from movie_cms.items import MoviesCmsItems

class MoviesSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['movie.thepan.cn']
    start_urls = [
        'https://movie.thepan.cn'
    ]

    rules = (
        Rule(LinkExtractor(allow=('details\.php',)), callback='parse_item'),
    )

    def parse_item(self, response):
        movie_item = MoviesCmsItems()
        movie_item['title'] = response.css('h2::text')[1].get().strip()
        movie_item['url'] = response.url
        movie_item['image'] = response.css('img').attrib['src']
        #Complete: finish the lines with the roght css selector 
        movie_item['year'] = response.css('p::text')[0].get().strip()
        movie_item['story'] = response.css('p::text')[1].get().strip()