import scrapy
import json
import os


class IETDAVVradeSpider(scrapy.Spider):
    name = "Gradesheet"

    def start_requests(self):
        # enter the build url here
        url = ''
        yield scrapy.Request(url=url, callback=self.parseGradesheet)

    def clean(self, s):
        # cleaning the page

    def parseGradesheet(self, response):
        page = response.url
        if page.split('/')[-1] == 'gradesheet.html':

        else:
            self.log('Wierd site %s', response.url)
