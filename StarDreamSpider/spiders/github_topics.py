import scrapy


class GithubTopicsSpider(scrapy.Spider):
    name = "github-topics"
    # start_urls = ["https://github.com/topics?page=1"]
    start_urls = [f"https://github.com/topics?page={page}" for page in range(1,10)]

    def parse(self, response):
        '''
        获取所有的a标签的链接，判断是否以 /topics/ 开头，是的话
        '''
        url_list=list(set(response.xpath('//a/@href').getall()))
        url_list=[url for url in url_list if url.startswith('/topics/') and len(url)>8]
        url_list=[response.urljoin(url) for url in url_list]
        print(url_list)
        for url in url_list:
            item={'topic_name':url.split('/')[-1],'topic_url':url}
            yield item
class GithubTopicsRepoSpider(scrapy.Spider):
    '''
    获取三页即可
    '''
    name = "github-topics_repo"
    start_urls = ["https://github.com/topics/ajax?o=desc&s=stars&page=1"]
    # start_urls = []

    def parse(self, response):
        '''
        找到页面的所有article
        '''
        articles=response.xpath('//article')
        for article in articles:
            repo_stars=article.xpath('.//*[@id="repo-stars-counter-star"]/text()').get()
            repo_url=response.urljoin(article.xpath('.//*[starts-with(@id, "code-tab")]/href').get())
            repo_topics=response.xpath('.//a[contains(@class, "topic-tag")')
            for repo_topic in repo_topics:
                topic_name=repo_topic.xpath('./text()').get()
                topic_url=response.urljoin(repo_topic.xpath('./@href').get())
        print(len(articles))