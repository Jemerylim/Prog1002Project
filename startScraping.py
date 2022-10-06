from urllib import response
from scrapy import spiderloader,signals
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from firebase import firebase
import json

settings = get_project_settings()
process = CrawlerProcess(settings)
spider_loader = spiderloader.SpiderLoader.from_settings(settings)
#print(spider_loader.list()[8:])
x = spider_loader.list()
x= x[3:8:3]
#auth = firebase.FirebaseAuthentication('ojtClYaLxeYUDxa8dgDaeP9P1X6CV9xtXDs8rFH7','limjeremy16@gmail.com')
fb_app = firebase.FirebaseApplication('https://hotel-review-f7091-default-rtdb.asia-southeast1.firebasedatabase.app/', authentication=None)
#print(x)
# for spider_name in x:
#     print("Running spider %s" % (spider_name))
process.crawl('ibis_style') 

def spider_ended(spider, reason):
    #print('xd')
    f = open('output.json')
    data = json.load(f)
    #print(data)
    for i in data:
        #print('lmao')
        datafield = {
            'reviewText':i['reviewText'],
            'reviewRating':i['reviewRating'],
            'reviewTitle':i['reviewTitle']
        }
        #print(datafield)
        name = '/'+str(spider.name)
        fb_app.post(name,datafield)
    f.close()


for crawler in process.crawlers:
    print('test')
    crawler.signals.connect(spider_ended, signal=signals.spider_closed)

process.start()
#