import scrapy

class ItabNewsSpider(scrapy.Spider):
    name = "itab_news"
    start_urls = ["https://api.codelife.cc/api/top/category?lang=cn"]
    def parse(self, response):
        print('response',response)
        pass
