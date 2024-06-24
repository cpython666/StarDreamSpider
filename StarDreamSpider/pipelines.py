# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class StardreamspiderPipeline:
    def process_item(self, item, spider):
        return item
from sqlalchemy.orm import sessionmaker
from yourproject.models import YourItemModel, db_connect, create_table

class SQLAlchemyPipeline:

    def open_spider(self, spider):
        database = spider.settings.get('DATABASE')
        self.engine = db_connect(database)
        create_table(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def close_spider(self, spider):
        self.engine.dispose()

    def process_item(self, item, spider):
        session = self.Session()
        your_item = YourItemModel()
        your_item.field1 = item['field1']
        your_item.field2 = item['field2']
        your_item.field3 = item['field3']

        try:
            session.add(your_item)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
