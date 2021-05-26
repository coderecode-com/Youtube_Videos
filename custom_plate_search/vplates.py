import scrapy
import pandas as pd
url = "https://vplates.com.au/vplatesapi/checkcombo?vehicleType=car&combination={}"


class VplatesSpider(scrapy.Spider):
    name = 'vplates'

    def start_requests(self):
        df = pd.read_csv('input.csv')
        for word in df['search'].tolist():
            yield scrapy.Request(url.format(word), cb_kwargs={'word': word})

    def parse(self, response, word):
        result = response.json().get("success")
        yield {
            'Word': word,
            'Available': 'Yes' if result else 'No'
        }
