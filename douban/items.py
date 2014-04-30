# coding: utf-8
from scrapy.item import Item, Field


class DoubanItem(Item):
    name = Field()              # 作品名称
    director = Field()          # 导演
    dramatist = Field()         # 编剧
    actors = Field()            # 主演
    tags = Field()              # 类型
    official_website = Field()  # 官网
    area = Field()              # 地区
    language = Field()          # 语言
    premiere = Field()          # 首映日期
    season = Field()            # 季度
    episodes = Field()          # 集数
    aka = Field()               # 又名
    description = Field()       # 简介
    imdb = Field()              # IMDB Link
