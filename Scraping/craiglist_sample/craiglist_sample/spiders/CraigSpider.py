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
#        titles = sel.xpath("//div[@class='content']")

# Downloading the file content under current directory.

        filename = 'search.txt'
        open(filename, 'wb').write(sel.xpath("//div[@class='content']").extract())


#        for title in titles:
#            title = title.xpath("a/text()").extract()
#            link = title.xpath("a/@href").extract()
#            print title, link
