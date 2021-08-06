import scrapy
from scrapy import FormRequest
import scraper_helper as sh


class HcidirectorySpider(scrapy.Spider):
    name = 'hcidirectory'
    start_urls = ['http://hcidirectory.sg/hcidirectory/']

    def parse(self, response):
        data = {
            'task': 'search',
            'RadioGroup1': 'HCI Name',
            'name': '',
            'clinicType': 'all'
        }
        yield FormRequest.from_response(response, formdata=data, callback=self.parse_page)

    def parse_page(self, response):
        for r in response.xpath('//*[@class="result_container"]'):
            item = {
                'Name': r.xpath('normalize-space(./*[@class="col1"]//a/text())').get(),
                'Phones': ', '.join([t.replace('\xa0', ' ') for t in r.xpath('normalize-space(./*[@class="col1"]//*[@class="tel"])').getall()]),
                'Address': r.xpath('normalize-space(./*[@class="col2"]//*[@class="add"])').get(),
                'Timing': r.xpath('normalize-space(./*[@class="col3"])').get()
            }
            yield item

        current_page = int(response.css('#targetPageNo ::attr(value)').get())
        total_page = int(response.css('#totalPage ::attr(value)').get())
        if current_page < total_page:
            data = {
                'task': 'search',
                'RadioGroup1': 'HCI Name',
                'name': '',
                'clinicType': 'all',
                'targetPageNo': str(current_page+1),
                'totalPage': str(total_page),
            }
            yield FormRequest.from_response(response, formdata=data, callback=self.parse_page)


if __name__ == '__main__':
    sh.run_spider(HcidirectorySpider)
