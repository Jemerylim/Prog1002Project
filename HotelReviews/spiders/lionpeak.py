import scrapy
from HotelReviews.items import HotelreviewsItem

class LionpeakSpider(scrapy.Spider):
    name = 'lion_peak'
    allowed_domains = ['www.tripadvisor.com.sg']
    start_urls = ['https://www.tripadvisor.com.sg/Hotel_Review-g294265-d15217860-Reviews-Lion_Peak_Hotel_Raffles-Singapore.html',]

    def parse(self, response):
        for review in response.xpath('//div[@class="WAllg _T"]'):
            item = HotelreviewsItem()
            item['reviewRating'] = review.xpath('./div[@class="IkECb f O"]/div[@class="Hlmiy F1"]/span').extract(),
            item['reviewTitle'] = review.xpath('./div[@class="KgQgP MC _S b S6 H5 _a"]/a[@class="Qwuub"]/span').extract(),
            item['reviewText'] = review.xpath('./div[@class="vTVDc"]/div[@class="_T FKffI bmUTE"]/div[@class="fIrGe _T"]/q[@class="QewHA H4 _a"]').extract()
            yield item
        next_page_url = response.xpath('//div[@class="MD"]/div[@class="ui_pagination is-centered"]/a[@class="ui_button nav next primary "]/@href').get()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))