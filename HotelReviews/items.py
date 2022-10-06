# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HotelreviewsItem(scrapy.Item):
    reviewText = scrapy.Field()
    reviewRating = scrapy.Field()
    reviewTitle = scrapy.Field()
    hotelName = scrapy.Field()

