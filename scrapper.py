import scrapy
import json
import os


class IITIGradeSpider(scrapy.Spider):
    name = "Gradesheet"

    def start_requests(self):
        # enter the build url here
        url = ''
        yield scrapy.Request(url=url, callback=self.parseGradesheet)

    def clean(self, s):

    def parseGradesheet(self, response):
        page = response.url
        if page.split('/')[-1] == 'gradesheet.html':

        else:
            self.log('Wierd site %s', response.url)
