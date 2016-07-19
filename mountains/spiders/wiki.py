# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import Selector
from urlparse import urljoin
from mountains.items import MountainItem

class WikiSpider(CrawlSpider):
    name = "wiki"
    allowed_domains = ["wikipedia.org"]
    start_urls = (
        'https://de.wikipedia.org/wiki/Kategorie:Berg_in_Tirol',
    )
    url = 'https://de.wikipedia.org/'
    rules = (Rule(LxmlLinkExtractor(allow=["/w/+"], restrict_xpaths=["//div[@id='mw-pages']"]), callback='parse_list',  follow=True),)

    def parse_next(self, response):
        yield Request(response.url, callback=self.parse_list)

    def parse_list(self, response):
        hrefs = Selector(response=response).xpath("//div[@class='mw-category']//a/@href")
        for href in hrefs:
            url = urljoin(self.url, href.extract())
            yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        item = MountainItem()
        item['url'] = response.url
        item['name'] = response.xpath('//h1/text()').extract()[0]
        item['photo'] = urljoin(self.url, response.xpath('//a[@class="image"]/@href').extract()[0])
        item['elevation'] = response.xpath(u"//tr[td/a[text()='Höhe']]/td[2]/span/text()").extract()[0].strip()
        map_links = response.xpath("//a[@class='external text']/@href").extract();
        if len(map_links) > 0:
            item['hasMap'] = 'https:' + map_links[0]
        item['latitude'] = response.xpath("//span[@title='Breitengrad']/text()").extract()[0] + response.xpath("//span[@title='Breitengrad']/abbr/text()").extract()[0]
        item['longitude'] = response.xpath(u"//span[@title='Längengrad']/text()").extract()[0] + response.xpath(u"//span[@title='Längengrad']/abbr/text()").extract()[0]
        yield item