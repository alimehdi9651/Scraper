import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime

class NoonYogaSpider(scrapy.Spider):
    name = 'noon_yoga_spider'
    start_urls = ['https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/']
    
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'noon_yoga_products.csv',
        'FEED_EXPORT_FIELDS': ['name', 'price', 'rating', 'url', 'date_extracted'],
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    def parse(self, response):
        products = response.css('div.sc-19767e73-1.fCFkgQ.grid')
        for product in products:
            yield {
                'name': product.css('span').get(),
                'price': product.css('strong.amount').get(),
                # 'rating': product.css('div.rating span::text').get(),
                'url': response.urljoin(product.css('a#productBox-N42326497A').get()),
                # 'date_extracted': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

        # next_page = response.css('a.next::attr(href)').get()
        # if next_page and len(products) < 200:
        #     yield response.follow(next_page, self.parse)

if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(NoonYogaSpider)
    process.start()