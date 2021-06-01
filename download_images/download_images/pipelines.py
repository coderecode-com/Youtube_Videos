from scrapy.pipelines.images import ImagesPipeline
import hashlib
from scrapy.utils.python import to_bytes
import re


class CustomImagesPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None, *, item=None):
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        product_name = item.get('product_name', image_guid)
        image_name = re.sub(r'[^\w]', '-', product_name.lower())
        return f'{image_name}.jpg'
