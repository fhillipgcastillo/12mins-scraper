import scrapy
import json
import logging
logger = logging.getLogger('mycustomlogger')

class TwelveminutesSpider(scrapy.Spider):
    name = 'twelveminutes'
    allowed_domains = ['blog.12min.com']
    links_file = open("./spiders/links.json")
    links_data = json.load(links_file)
    # start_urls = ["https://blog.12min.com/leadershift-pdf-summary/"]
    start_urls = [data["link"] for data in links_data]
    
    def parse(self, response):
        for page in response.xpath('/html/body/div/div/div/main/article'):
            title = page.css('h1.entry-title::text').get()
            content = "\n".join(page.css('.article-content > h2, .article-content > h3, .article-content > p').xpath('text()').getall())
            yield {
                'title': title,
                'content': content,
                # 'cover': page.css('figure > img@src').get(),
                'url': response.url,
            }
            
            # optional for the future
            # self.save_text_file(title, content)
            
    def save_text_file(self, title, content):
        filename = f'page - {title}.txt'
        with open(filename, 'wb') as f:
            f.write(content.encode())
        logger.info(f'Saved file {filename}')
            

