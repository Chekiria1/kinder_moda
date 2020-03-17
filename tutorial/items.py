# -*- coding: utf-8 -*-
from scrapy.item import Item, Field
from scrapy.loader.processors import TakeFirst, Join, MapCompose
import re


def clear_text(text):
    # strip the unicode quotes
    text = re.sub(r'\s{1,}$', '', text)
    text = re.sub(r'^.*:\s', '', text)
    return text

def to_int(text):
    text = int(re.sub(' ', '', text))
    return text

def clear_to_int(text):
    text = re.sub(r'\s{1,}$', '', text)
    text = int(re.sub(r'^.*:\s', '', text))
    return text

def clear_size(text):

    text = re.sub(r'\s{1,}', '', text)
    text = re.sub(r'\n', '', text)

    #str1 = ""


    #str1 = ''.join(text)


    # return string
    #return (', '.join(text))
    return text.strip('[]') #str(text)

class kinderItem(Item):
    crawled_date = Field(output_processor=TakeFirst())
    url = Field(output_processor=TakeFirst())
    brand = Field(input_processor=MapCompose(clear_text), output_processor=TakeFirst())
    item_id = Field(input_processor=MapCompose(clear_to_int), output_processor=TakeFirst())
    #size = Field(output_processor=TakeFirst())
    title = Field(output_processor=TakeFirst())
    img = Field(output_processor=TakeFirst())

#class sizePrise(Item):

    price_reg_1 = Field(input_processor=MapCompose(to_int), output_processor=TakeFirst())
    price_end_1 = Field(input_processor=MapCompose(to_int), output_processor=TakeFirst())
    price_reg_2 = Field(input_processor=MapCompose(to_int), output_processor=TakeFirst())
    price_end_2 = Field(input_processor=MapCompose(to_int), output_processor=TakeFirst())
    price_reg_3 = Field(input_processor=MapCompose(to_int), output_processor=TakeFirst())
    price_end_3 = Field(input_processor=MapCompose(to_int), output_processor=TakeFirst())
    price_reg_4 = Field(input_processor=MapCompose(to_int), output_processor=TakeFirst())
    price_end_4 = Field(input_processor=MapCompose(to_int), output_processor=TakeFirst())

    size_in_stoke_1 = Field(input_processor=MapCompose(clear_size))

    #size_out_stoke_1 = Field(input_processor=MapCompose(clear_size))
    size_in_stoke_2 = Field(input_processor=MapCompose(clear_size))
    #size_out_stoke_2 = Field(input_processor=MapCompose(clear_size))
    size_in_stoke_3 = Field(input_processor=MapCompose(clear_size))
   # size_out_stoke_3 = Field(input_processor=MapCompose(clear_size))
    size_in_stoke_4 = Field(input_processor=MapCompose(clear_size))
    #size_out_stoke_4 = Field(input_processor=MapCompose(clear_size))






