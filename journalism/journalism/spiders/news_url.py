# -*- coding: utf-8 -*-
import scrapy


class NewsUrlSpider(scrapy.Spider):
    name = 'news_url'
    allowed_domains = ['news.hao123.com']
    start_urls = ['http://news.hao123.com/wangzhi/']

    def parse(self, response):
        web_urls = response.xpath('//h3/div//a/@href')


