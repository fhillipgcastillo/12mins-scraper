import scrapy
import json
import logging
logger = logging.getLogger('mycustomlogger')

class TwelveminutesSpider(scrapy.Spider):
    name = 'twelveminutes'
    allowed_domains = ['blog.12min.com']
    links_file = open("./spiders/links.json")
    links_data = json.load(links_file)
    # start_urls = ["cache:https://blog.12min.com/leadershift-pdf-summary/"] # wip
    # start_urls = ["https://blog.12min.com/leadershift-pdf-summary/"]
    start_urls = [data["link"] for data in links_data]
    custom_settings = {
        'FEED_FORMAT' : "csv",
        'FEED_URI' : 'tmp/shopclues.csv',
    }
    
    def parse(self, response):
        for page in response.xpath('//*[@id="main"]'):
            title = page.css('h1.entry-title::text').get()
            cover = page.css('figure img::attr(data-src)').get()
            content = "\n".join(page.css('.article-content > h2, .article-content > h3, .article-content > p').xpath('text()').getall())
            
            yield {
                'title': title,
                'url': response.url,
                'cover': cover,
                'content': content,
            }
            
            # optional for the future
            # self.save_text_file(title, content)
            
    def save_text_file(self, title, content):
        filename = f'page - {title}.txt'
        with open(filename, 'wb') as f:
            f.write(content.encode())
        logger.info(f'Saved file {filename}')
            

