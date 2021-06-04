import re
from urllib.parse import urlparse

from scrapy.exceptions import CloseSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


def extract_emails(s) -> list:
    pattern = r"\b[\w\._]+@[\w\._]+\b"
    return re.findall(pattern, s, )


class EmailExtractSpider(CrawlSpider):
    name = 'email_extract'

    def __init__(self, name=None, **kwargs):
        if 'sites' in kwargs:
            self.start_urls = kwargs.get('sites').split(',')
            self.allowed_domains = [urlparse(x).netloc for x in self.start_urls]
        else:
            raise CloseSpider("Argument sites not found")

        super().__init__(name=name, **kwargs)

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    # rules = (
    #     Rule(LinkExtractor(allow=(
    #         '/contact',
    #         '/contact-us',
    #         '/contact-me'
    #         '/about',
    #         '/about-me',
    #         '/about-us',
    #     )), callback='parse_item', follow=True),
    # )

    def parse_item(self, response):
        for mail in extract_emails(response.text):
            yield {
                'emails': mail,
                'source': response.url
            }
