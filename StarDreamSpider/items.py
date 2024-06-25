import scrapy


class GitHubTopicItem(scrapy.Item):
	topic_url = scrapy.Field()
	topic_name = scrapy.Field()
	topic_description = scrapy.Field()
	topic_chinese_description = scrapy.Field()
	
	info_title = scrapy.Field()
	info_description = scrapy.Field()
	info_chinese_description = scrapy.Field()
	info_url = scrapy.Field()
	info_logo_url = scrapy.Field()
