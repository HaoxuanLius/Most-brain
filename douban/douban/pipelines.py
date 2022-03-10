# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from openpyxl import Workbook


class DoubanPipeline:
    def __init__(self) -> None:
        self.file=Workbook()
        self.avi=self.file.active
    
    def process_item(self, item, spider):
        self.avi.append([item['name'],item['daoy'],item['time']])

        return item
    def close_spider(self,spider):
        self.file.save(r'e:\Users\yrfs\Desktop\chai.xlsx')
        self.file.close()