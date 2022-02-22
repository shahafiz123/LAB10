import scrapy


class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['https://brickset.com/sets/year-2017']

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }

# To recurse next page
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
          yield scrapy.Request(
              response.urljoin(next_page),
              callback=self.parse
         )


import scrapy


class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['https://brickset.com/sets/year-2018']

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }

# To recurse next page
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
          yield scrapy.Request(
              response.urljoin(next_page),
              callback=self.parse
         )