import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    start_urls = ['https://techinstr.myshopify.com/collections/all']

    def parse(self, response):
        # .product-card > a
        for link in response.css('.product-card > a ::attr(href)').getall():
            yield response.follow(link, callback=self.parse_product)

        next_page = response.css('.pagination li:last-child a ::attr(href)').get()
        if next_page:
            yield response.follow(next_page)  # default callback is parse

    def parse_product(self, response):
        links = response.css('noscript > img ::attr(src)').getall()
        links = [response.urljoin(link) for link in links]
        product_name = response.css('h1 ::text').get()
        yield {
            'image_urls': links,
            'product_name': product_name
        }
