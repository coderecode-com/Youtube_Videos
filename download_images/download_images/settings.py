BOT_NAME = 'download_images'
SPIDER_MODULES = ['download_images.spiders']
NEWSPIDER_MODULE = 'download_images.spiders'
ROBOTSTXT_OBEY = True
# ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
ITEM_PIPELINES = {'download_images.pipelines.CustomImagesPipeline': 1}

IMAGES_STORE = 'product_images'
