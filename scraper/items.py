# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field


class ScrapedArticle(Item):
    title = Field()
    subtitle = Field()
    authors = Field()
    section = Field()
    image = Field()
    content = Field()
    slug = Field()
    created_on = Field()