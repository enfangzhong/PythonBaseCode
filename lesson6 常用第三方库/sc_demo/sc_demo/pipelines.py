# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScDemoPipeline(object):
    def process_item(self, item, spider):
        return item

class S17huoPipeLine(object):
    f = None
    def open_spider(self, spider):
        S17huoPipeLine.f = open('s17huo.csv', 'w+', encoding='utf-8')
        
    def close_spider(self, spider):
        if S17huoPipeLine.f:
            S17huoPipeLine.f.close()
            
    def process_item(self, item, spider):
        '''
        print('%s: %s, %s' % (spider.name, item['title'], item['price']))
        return item
        '''
        if float(item['price']) < 60.0:
            S17huoPipeLine.f.write('%s, %s\n' % (item['title'], item['price']))