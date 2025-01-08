# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjetscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    nom = scrapy.Field()
    prix = scrapy.Field()
    lien = scrapy.Field()
    
