# from sqlalchemy.orm import sessionmaker
# # from StarDreamSpider.models import GitHubTopics, GitHubTopicsInfo, db_connect, create_table
#
#
# class GithubTopicsPipeline:
#
# 	def open_spider(self, spider):
# 		database = spider.settings.get('DATABASE')
# 		self.engine = db_connect(database)
# 		create_table(self.engine)
# 		self.Session = sessionmaker(bind=self.engine)
#
# 	def close_spider(self, spider):
# 		self.engine.dispose()
#
# 	def process_item(self, item, spider):
# 		session = self.Session()
#
# 		# 处理 GitHubTopics
# 		topic = session.query(GitHubTopics).filter_by(url=item['topic_url']).first()
# 		if not topic:
# 			topic = GitHubTopics()
# 			topic.url = item['topic_url']
# 			topic.name = item['topic_name']
# 			topic.description = item['topic_description']
# 			topic.chinese_description = item.get('topic_chinese_description', '')
# 			session.add(topic)
#
# 		# 处理 GitHubTopicsInfo
# 		info = GitHubTopicsInfo()
# 		info.title = item['info_title']
# 		info.description = item['info_description']
# 		info.chinese_description = item.get('info_chinese_description', '')
# 		info.url = item['info_url']
# 		info.logo_url = item['info_logo_url']
#
# 		info.topics.append(topic)
# 		session.add(info)
#
# 		try:
# 			session.commit()
# 		except:
# 			session.rollback()
# 			raise
# 		finally:
# 			session.close()
#
# 		return item
