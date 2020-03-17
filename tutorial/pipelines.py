# -*- coding: utf-8 -*-
import json
from sqlalchemy.orm import sessionmaker
from tutorial.models import Products,Price, db_connect, create_table
import logging
from time import gmtime, strftime
from scrapy.exceptions import DropItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

class DefaultValuesPipeline(object):
    def process_item(self, item, spider):
        for field in item.fields:
            item.setdefault(field, 'None')
        return item

'''class ClearBrandPipline(object):
    def process_item(self, item, spider):
        for field in item.fields:
            item.setdefault(field, 'None')
        return item'''


class JsonPipeline(object):
    def open_spider(self, spider):
        self.file = open('kinder {}.json'.format(strftime("%Y-%m-%d %H_%M_%S", gmtime())), 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


'''class CsvPipeline(object):
    def open_spider(self, spider):
        self.file = open('kinder {}.csv'.format(strftime("%Y-%m-%d %H_%M_%S", gmtime())), 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write(str(item))
        return item'''





class SaveQuotesPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        logging.info("****SaveQuotePipeline: database connected****")

    def process_item(self, item, spider):
        """Save quotes in the database
        This method is called for every item pipeline component
        """

        session = self.Session()
        products = Products()
        price = Price()
        products.url = item["url"]
        products.title = item["title"]
        products.brand = item["brand"]
        products.item_id = item["item_id"]
        products.img = item["img"]
        #kinder.size = item["size"]
        price.item_id = item["item_id"]
        price.price_reg_1 = item["price_reg_1"]
        price.price_end_1 = item["price_end_1"]
        price.price_reg_2 = item["price_reg_2"]
        price.price_end_2 = item["price_end_2"]
        price.price_reg_3 = item["price_reg_3"]
        price.price_end_3 = item["price_end_3"]
        price.price_reg_4 = item["price_reg_4"]
        price.price_end_4 = item["price_end_4"]
        '''price.size_in_stoke_1 = item["size_in_stoke_1"]
        price.size_in_stoke_2 = item["size_in_stoke_2"]
        price.size_in_stoke_3 = item["size_in_stoke_3"]
        price.size_in_stoke_4 = item["size_in_stoke_4"]'''

        try:
            session.add(products)
            session.add(price)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item




class DuplicatesPipeline(object):

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates tables.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        logging.info("****DuplicatesPipeline: database connected****")

    def process_item(self, item, spider):
        session = self.Session()

        #exist_item_id = session.query(Products).filter_by(item_id=item["item_id"]).first()
        exist_item = session.query(Price).filter_by(item_id=item["item_id"], price_end_1=item["price_end_1"], price_end_2=item["price_end_2"], price_end_3=item["price_end_3"], price_end_4=item["price_end_4"]).first()
        if exist_item is not None:  # the current quote exists
            #raise DropItem("Duplicate item found: %s" % item["item_id"])
            raise DropItem("Duplicate item found: {}, {}, {}, {}, {}".format(item["item_id"], item["price_end_1"], item["price_end_2"], item["price_end_3"], item["price_end_4"]))
            session.close()
        else:
            return item
            session.close()