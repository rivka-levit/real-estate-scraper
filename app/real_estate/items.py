# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader.processors import MapCompose, Join


def description_in(descr):
    """
    Function for input processor.

    Args:
        descr (str): item received from item loader

    Returns:
        str: item without spaces
    """

    return descr.strip()


def description_out(descr):
    """
    Function for output processor.

    Args:
        descr (list): item values received and processed by item loader

    Returns:
        dict: structured item values to output
    """

    labels = descr[:3]
    values = descr[3:]
    output = {
        labels[0]: ''.join(values[0]),
        labels[1]: '; '.join(values[1:-1]),
        labels[2]: ''.join(values[-1])
    }

    return output


class RealEstateItem(scrapy.Item):
    name = scrapy.Field(output_processor=Join())
    description = scrapy.Field(
        input_processor=MapCompose(description_in),
        output_processor=description_out
    )
    price = scrapy.Field(output_processor=Join())
    agency = scrapy.Field(output_processor=Join())
