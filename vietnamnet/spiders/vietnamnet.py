# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class JobsSpider(scrapy.Spider):
    name = 'vietnamnet'
    start_urls = []

    def start_requests(self):
        urlRelative = 'https://vietnamnet.vn/da-nang-ngap-khap-nga-nguoi-dan-kho-so-dat-xe-chet-may-'
        count = 0
        for page in range(2198000, 2201720):
            count = count + 1
            url = urlRelative + str(page)+'.html'
            print(url)
            print('page - ', count)
            yield scrapy.Request(url, self.parse)


    def parse(self, response):
            title = response.xpath('//title/text()').get()
            time = response.xpath("//div[@class='bread-crumb-detail__time']/text()").get()
            time = time.strip(" \r\n")
            response = str(response)
            response = response.lstrip("<HtmlResponse200")
            response = response.lstrip("<200 ")
            link = response.strip(">")
            record = {'title': title, 'time': time, 'link': link}
            yield record
