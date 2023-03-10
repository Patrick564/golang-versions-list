# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VersionsItem(scrapy.Item):
    versions = scrapy.Field()


class SelectedVersionItem(scrapy.Item):
    filename = scrapy.Field()
    size = scrapy.Field()
    checksum = scrapy.Field()


class SelectedVersionListItem(scrapy.Item):
    all_versions = scrapy.Field()
