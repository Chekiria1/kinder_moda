from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.twisted import TwistedScheduler
from tutorial.spiders.kinder_spider import JobSpider

process = CrawlerProcess(get_project_settings())
scheduler = TwistedScheduler()
scheduler.add_job(process.crawl, 'cron', args=[JobSpider], hour='12', minute='13')
scheduler.start()
process.start(False)
