# New File

from scrapy.spider import Spider
from scrapy.selector import Selector
from craiglist_sample.items import CraiglistSampleItem


class CraigSpider(Spider):
    """this is cool"""

    name = "CraigSpider"
    allowed_domains = ["craiglist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/jjj?zoomToPosting=&catAbb=jjj&query=data+scientist&excats="]

    def parse(self, response):
        sel = Selector(response)

        titles = sel.xpath("//div[@class='content']/p[@class='row']")
        items = []
        for title in titles:
            item = CraiglistSampleItem()
            item['date'] = title.xpath(".//span[@class='date']/text()").extract()
            item['link'] = title.xpath("a/@href").extract()
            item['name'] = title.xpath(".//a[2]/text()").extract()
            items.append(item)
        return items
