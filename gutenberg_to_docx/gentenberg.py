import scrapy
from h2d import Document
from h2d import HtmlToDocx
import scraper_helper


class GentenbergSpider(scrapy.Spider):
    name = 'gentenberg'
    # allowed_domains = ['x']
    start_urls = ['https://www.gutenberg.org/browse/scores/top#books-last30']

    def parse(self, response):
        css = 'ol:nth-child(18) li a:last-child ::attr(href)'
        links = response.css(css).getall()
        for link in links:
            yield response.follow(link, callback=self.parse_book_summary)
            

    def parse_book_summary(self, response):
        xpath = '//a[contains(text(), "Read this book online") and contains(text(),"HTML")]/@href'
        url = response.xpath(xpath).get()
        if url:
            yield response.follow(url, callback=self.parse_book)

    def parse_book(self, response):
        document = Document()
        new_parser = HtmlToDocx()
        new_parser.options['images']=False
        book_title= response.xpath("//h1").xpath("normalize-space(.)").get()
        html = f"<h1>{book_title}</h1>"
        html += ''.join(response.xpath(
            '//h1/following-sibling::div[@class="chapter"]').getall())
        new_parser.add_html_to_document(html, document)
        document.save(
            f'{book_title}.docx')
        print(f'{book_title}.docx')


scraper_helper.run_spider(GentenbergSpider)
