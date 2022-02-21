import scrapy
from ..items import WorkItem

class LondonrenSpider(scrapy.Spider):
    name = 'londonren'
    page_number = 2
    start_urls = ['https://londonrelocation.com/our-properties-to-rent/properties/']

    def parse(self, response):
        items = WorkItem()
        address = response.css('.h4-space a::text').extract()
        price = response.css('h5::text').extract()
        link = response.css('.h4-space a::attr(href)').extract()
        link = ['https://londonrelocation.com'+url
        for url in link]
        items['address'] = address
        items['price'] = price
        items['link'] = link
        yield items
        next_page = 'https://londonrelocation.com/our-properties-to-rent/properties/?pageset='+str(LondonrenSpider.page_number)
        if LondonrenSpider.page_number <= 5: #scraping 5 pages
            LondonrenSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)