# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy import FormRequest
from scrapy import Request

formdata = {'form_email':'regdzz.lin@gmail.com',
            'form_password':'Julyedu123!'}
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
headers ={'user-agent':ua}

# Cookie登陆
cookies = {'bid': 'a3MhK2YEpZw', 'll': '"108296"', 'gr_user_id': '0b04b3f6-fab4-4b70-86df-38982c6d0535', '__yadk_uid': '6X9uTW4XzeoQErRmSRzwy0DuKnot3o6l', 'viewed': '"26859889_25923638_3081930_3924175_20471211_1057390_26829015_25716519_3715623_26836700"', '_vwo_uuid_v2': '64E0E442544CB2FE2D322C59F01F1115|026be912d24071903cb0ed891ae9af65', 'ps': 'y', 'ue': '"regdzz.lin@gmail.com"', 'ap': '1', '_ga': 'GA1.2.1329310863.1477654711', '_gid': 'GA1.2.1512376980.1507810106', 'ck': 'BJYG', 'push_noty_num': '0', 'push_doumail_num': '0', '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1507815681%2C%22https%3A%2F%2Fwww.google.co.jp%2F%22%5D', '_pk_id.100001.8cb4': '40c3cee75022c8e1.1477654710.48.1507815681.1507813082.', '_pk_ses.100001.8cb4': '*', '__utmt': '1', '__utma': '30149280.1329310863.1477654711.1507813051.1507815686.67', '__utmb': '30149280.1.10.1507815686', '__utmc': '30149280', '__utmz': '30149280.1498663983.61.43.utmcsr', '__utmv': '30149280.16399', 'dbcl2': '"163994952:P/K0jZvrIGY"'}

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com']

    def start_requests(self):
        for url in DoubanSpider.start_urls:
            yield Request(url, headers=headers, cookies=cookies, callback=self.parse)

    def parse(self, response):
        print(response.text)

'''
# 用户名/密码登陆
class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    my_start_urls = ['http://www.douban.com/'] # 因为我实现了start_requests，所欲可以改名。

    def start_requests(self):
        for url in DoubanSpider.my_start_urls:
            formdata['redir'] = url
            yield FormRequest('https://accounts.douban.com/login',
                              headers=headers,
                              formdata=formdata,
                              callback=self.parse)
    
    def parse(self, response):
        bs = BeautifulSoup(response.text, 'html5lib')
        captcha = bs.select('img#captcha_image')
        if captcha:
            captcha = captcha[0]
            # 处理验证码
            img_url = captcha.get('src').strip()
            print(img_url)
            id_ = img_url.split('?')[1].split('&')[0].split('=')[1]
            text = input('请输入验证码')
            formdata['captcha-solution'] = text
            formdata['captcha-id'] = id_
            yield FormRequest.from_response(response, formdata=formdata, headers=headers, callback=self.parse)
        else:
            print(response.text)
'''
