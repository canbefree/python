# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
import os
from selenium import webdriver
import time

from difa.items import DifaItem

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?wd=%E8%92%82%E6%B3%95']

    def __init__(self):
        self.driver = webdriver.Chrome()

    # def parse

    def parse(self, response):
        # f = open('test.txt',"w+")
        # inspect_response(response,self)
        # f.write(response.body)
        # time.sleep(2)
    
        # self.driver.find_element_by_xpath("//div[@id='page']/a[last()]").click()
        url = "https://www.baidu.com" + response.xpath("//div[@id='page']/a[last()]/@href").extract_first()
        yield scrapy.Request(url,callback=self.parse)

        item = DifaItem()
        item["imagesize"] = 123123
        yield item