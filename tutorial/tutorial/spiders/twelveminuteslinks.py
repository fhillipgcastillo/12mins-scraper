import scrapy


class TwelveminuteslinksSpider(scrapy.Spider):
    name = 'twelveminuteslinks'
    allowed_domains = ['blog.12min.com']
    start_urls = ['http://blog.12min.com/']
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
     
    def start_requests(self):
        yield scrapy.Request(url="http://blog.12min.com/", headers={
            'Uger-Agent': self.user_agent
        })
        
    def parse(self, response):
        for page in response.css('#main article.type-post'):
            yield {
                'title': page.xpath('div/div/section/h3/a/text()').get(),
                'link': page.xpath('div/div/section/h3/a/@href').get(),
                'cover': page.xpath('div/header/div/a/img/@src').get(),
                'text_preview': page.xpath('div/div/section/div/p/text()').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        # next_page = None
        
        if next_page is not None:
            yield response.follow(next_page, self.parse)
