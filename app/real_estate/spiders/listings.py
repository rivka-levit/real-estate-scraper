import scrapy

from real_estate.items import RealEstateItem


class ListingsSpider(scrapy.Spider):
    name = "listings"
    allowed_domains = ["www.arizonarealestate.com"]
    start_urls = [
        "https://www.arizonarealestate.com/maricopa",
        "https://www.arizonarealestate.com/goodyear",
        "https://www.arizonarealestate.com/tempe"
    ]

    def parse(self, response, **kwargs):
        gallery = response.xpath('//div[@class="si-listings-column"]')

        item = RealEstateItem()

        for listing in gallery:
            item['name'] = listing.xpath(
                './/div[@class="si-listing__title-main"]/text() | '
                './/div[@class="si-listing__neighborhood"]/'
                'span[@class="si-listing__neighborhood-place"]/text()'
            ).getall()
            item['description'] = listing.xpath(
                './/div[@class="si-listing__info-label"]/text() | '
                './/div[@class="si-listing__info-value"]/descendant::*/text()'
            ).getall()

            # Get rid of extra spaces
            item['description'] = [
                ''.join(x.split()) for x in item['description']
            ]

            item['price'] = listing.xpath(
                './/div[@class="si-listing__photo-price"]/span/text()'
            ).get()
            item['agency'] = listing.xpath(
                './/div[@class="si-listing__footer"]/div/text()'
            ).get()

            yield item
