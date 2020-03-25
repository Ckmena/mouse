import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from movies_cms.items import MoviesCmsItem

# <<<<<<< HEAD
class MoviesSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['movie.thepan.cn']
# =======

class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ["movie.thepan.cn"]
# >>>>>>> ed9496ec1e9ce0fefed0130b68d501b860798112
    start_urls = [
        'https://movie.thepan.cn'
    ]

    rules = (
        Rule(LinkExtractor(allow=('details\.php',)), callback='parse_item'),
    )

    def parse_item(self, response):
        movie_item = MoviesCmsItem()
        movie_item['title'] = response.css('h2::text')[1].get().strip()
        movie_item['url'] = response.url
        movie_item['image'] = response.css('img').attrib['src']
# <<<<<<< HEAD
        #Complete: finish the lines with the roght css selector 
        movie_item['year'] = response.css('p::text')[0].get().strip()
        movie_item['story'] = response.css('p::text')[1].get().strip()
        yield movie_item

        #https://movie.thepan.cn/details.php?id=1
# =======
        movie_item['year'] = response.css('p::text')[0].get().strip()
        movie_item['story'] = response.css('p::text')[1].get().strip()
        yield movie_item
# >>>>>>> ed9496ec1e9ce0fefed0130b68d501b860798112
