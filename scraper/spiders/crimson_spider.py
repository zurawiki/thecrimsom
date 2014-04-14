from datetime import datetime

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.selector import Selector

from scraper.items import ScrapedArticle


__author__ = 'roger'


class CrimsonLinkExtractor(SgmlLinkExtractor):
    def extract_links(self, response):
        ret = SgmlLinkExtractor.extract_links(self, response)
        for link in ret:
            link.url += "?page=single"

        return ret


class CrimsonSpider(CrawlSpider):
    name = "crimson"
    allowed_domains = ["www.thecrimson.com"]
    start_urls = [
        "http://www.thecrimson.com/",
        "http://www.thecrimson.com/section/news/",
        "http://www.thecrimson.com/section/opinion/",
        "http://www.thecrimson.com/section/fm/",
        "http://www.thecrimson.com/section/sports/",
        "http://www.thecrimson.com/section/media/",
        "http://www.thecrimson.com/section/arts/",
        "http://www.thecrimson.com/section/flyby/",
        "http://www.thecrimson.com/admissions/",
    ]

    rules = [Rule(CrimsonLinkExtractor(allow=('/article/\d+/\d+/\d+/',)), callback="parse_article", follow=False)]

    def parse_article(self, response):
        sel = Selector(response)
        a = sel.css('#article')
        if a:
            a = a[0]
        else:
            return None

        subtitle = a.css("#article-header h2::text").extract()
        if subtitle:
            subtitle = subtitle[0]
        else:
            subtitle = ''
        item = {
            "title": a.css("#article-header h1::text").extract()[0],
            "subtitle": subtitle,
            "authors": a.css(".article-byline a::text").extract(),
            "section": sel.css("li a.active::text").extract()[0],
            "image": a.select("//img/@src").extract(),
            "content": a.css("#text").extract()[0],
            "slug": response.url.split('/')[-2],
            "created_on": datetime.strptime(a.select("//time/@datetime").extract()[0].split('T')[0], "%Y-%m-%d"),
        }
        article = ScrapedArticle(**item)
        return article

