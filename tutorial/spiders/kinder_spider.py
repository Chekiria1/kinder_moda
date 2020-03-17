# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from tutorial.items import kinderItem


class KinderSpider(scrapy.Spider):
    name = "kinder"
    allowed_domain = ["kinder-moda.com.ua"]
    start_urls = ['https://kinder-moda.com.ua/boys/boys-sale/?sort=p.date_added&order=DESC']

    def parse(self, response):
        '''for i in range(0, 1):
            yield response.follow('https://www.levi.com/US/en_US/sale/c/levi_clothing_sale_us/sort/latest-arrival?page=' + str(i))###, self.parse_job)'''
        product_items = response.xpath("//div[@class='item_block']")
        #product_items = response.css("div.product-item")
        #product_items = response.xpath("//div[@class='product__listing product__grid']")
        urls = response.xpath(".//span[@class='item_title']/a/@href").getall()
        for url in urls:
            #page_url = 'https://dejobs.org' + url
            yield response.follow(url, self.parse_item)

        #for pi in product_items:
            #loader = ItemLoader(item=kinderItem(), selector=pi)
            #loader.add_value('url', response.url)
            #loader.add_xpath('url', ".//span[@class='item_title']/a/@href")
            #yield response.follow(page_url, self.parse_item)

    def parse_item(self, response):
        loader = ItemLoader(item=kinderItem(), response=response)
        loader.add_value('url', response.url)
        loader.add_xpath('brand', ".//div[@class='prod_title_block']/p[1]/text()")
        loader.add_xpath('item_id', ".//div[@class='prod_title_block']/p[2]/text()")
        loader.add_xpath('img', ".//div/div/a[@class='thumbnail MagicZoom']/@href")
        #loader.add_xpath('img', ".//div[@class='product_img_slider']/div/div/a[@class='thumbnail MagicZoom']/@href")

        loader.add_xpath('size_in_stoke_1', ".//div[@class='choise_size'][1]/div[@class='label_block']//text()")
        #self.logger.info('aaaa ----- {}'.format(response.xpath(".//div[@class='choise_size'][1]/div[@class='label_block']//text()")))
        #loader.add_xpath('size_out_stoke_1', ".//div[@class='item_desc']/p[2]/text()")
        loader.add_xpath('size_in_stoke_2', ".//div[@class='choise_size'][2]/div[@class='label_block']//text()")
        #loader.add_xpath('size_out_stoke_2', ".//div[@class='item_desc']/p[2]/text()")
        loader.add_xpath('size_in_stoke_3', ".//div[@class='choise_size'][3]/div[@class='label_block']//text()")
        #loader.add_xpath('size_out_stoke_3', ".//div[@class='item_desc']/p[2]/text()")
        loader.add_xpath('size_in_stoke_4', ".//div[@class='choise_size'][4]/div[@class='label_block']//text()")
        #loader.add_xpath('size_out_stoke_4', ".//div[@class='item_desc']/p[2]/text()")
        #loader.add_xpath('stoke_1', ".//div[@class='item_desc']/p[2]/text()")'''



        loader.add_xpath('title', ".//div[@class='prod_title_block']/h1/text()")

        loader.add_xpath('price_reg_1', ".//div[@class='choise_size'][1]/div[@class='choise_size_cost']/span[@class='old_price']/b/text()")
        loader.add_xpath('price_end_1', ".//div[@class='choise_size'][1]/div[@class='choise_size_cost']/span[@class='current_price']/b/text()")
        loader.add_xpath('price_reg_2',  ".//div[@class='choise_size'][2]/div[@class='choise_size_cost']/span[@class='old_price']/b/text()")
        loader.add_xpath('price_end_2', ".//div[@class='choise_size'][2]/div[@class='choise_size_cost']/span[@class='current_price']/b/text()")


        loader.add_xpath('price_reg_3',  ".//div[@class='choise_size'][3]/div[@class='choise_size_cost']/span[@class='old_price']/b/text()")
        loader.add_xpath('price_end_3', ".//div[@class='choise_size'][3]/div[@class='choise_size_cost']/span[@class='current_price']/b/text()")
        loader.add_xpath('price_reg_4', ".//div[@class='choise_size'][4]/div[@class='choise_size_cost']/span[@class='old_price']/b/text()")
        loader.add_xpath('price_end_4', ".//div[@class='choise_size'][4]/div[@class='choise_size_cost']/span[@class='current_price']/b/text()")
        yield loader.load_item()






