# -*- coding: utf-8 -*-
import scrapy
from ..items import S17huoItem


class S17huoSpider(scrapy.Spider):
    name = "s17huo"
    allowed_domains = ["17huo.com"]
    start_urls = ['http://www.17huo.com/list-man-0-50011123-0--2m0.html']
    pages = 0

    def parse(self, response):
        products = response.css('ul.item > li')
        for product in products:
            title = product.css('a > p.item_title::text')[0].extract().strip()
            price = product.css('a > div.item_info > span::text')[0].extract()[1:].strip()
            # item = S17huoItem(title=title, price=price)
            yield {'title':title, 'price':price} # 扔字典和扔item对象是等价的
        S17huoSpider.pages += 1
        if S17huoSpider.pages >= 3:
            return
        pages = response.css('div.pagem.product_list_pager > a')
        next_page = pages[-2]
        if next_page.css('font.page_down'):
            next_page = next_page.css('::attr(href)')[0].extract().strip()
            yield scrapy.Request(next_page, callback=self.parse)