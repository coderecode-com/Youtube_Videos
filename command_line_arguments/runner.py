import argparse

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from args.spiders.email_extract import EmailExtractSpider


def main(sites):
    settings = get_project_settings()
    settings['FEEDS'] = {
        'extracted_emails.csv': {
            'format': 'csv',
            'overwrite': False,
        },
    }
    process = CrawlerProcess(settings)

    process.crawl(EmailExtractSpider, sites=sites)
    process.start()
    print("\n\nDONE")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--sites", help="Enter comma separated website URLs without space ")

    args = parser.parse_args()

    if args.sites:
        main(args.sites)
    else:
        print("Missing Required Arguments:\n\t-s SITES"
              "https://example1.com,https://example2.com")
