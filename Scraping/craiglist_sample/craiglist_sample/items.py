# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CraiglistSampleItem(Item):
    date = Field()
    link = Field()
    name = Field()
    # define the fields for your item here like:
    # name = Field()
