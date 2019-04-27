# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class JimmySpider(scrapy.Spider):
    name = "jimmy"
    allowed_domains = ["jimmychoo.com"]
    start_urls = ['http://row.jimmychoo.com/en/women/shoes/boots/']

    def parse(self, response):
        bs = BeautifulSoup(response.text, 'html5lib')
        elements = bs.select('ul#product-search-result-items > li > article > div > a.js-producttile_link')
        for element in elements:
            product_url = 'http://row.jimmychoo.com/' + element.get('href').strip()
            yield scrapy.Request(product_url, callback=self.parse_product)   

    def parse_product(self, response):
        yield {'url':response.url}
