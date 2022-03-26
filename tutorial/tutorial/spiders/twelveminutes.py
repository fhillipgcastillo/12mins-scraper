import scrapy


class TwelveminutesSpider(scrapy.Spider):
    name = 'twelveminutes'
    allowed_domains = ['blog.12min.com']
    start_urls = ['http://blog.12min.com/']

    def parse(self, response):
        pass
