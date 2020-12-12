import scrapy
import json
import os


class IETDAVVGradeSpider(scrapy.Spider):
    name = "Gradesheet"

    def start_requests(self):
        # enter the build url here
        codes = ['C','V','I','E','T','M']
        batches = ['0','1']
        nums = [i for i in range(1,100)]
        years = [('19','2'),('18','4'),('17','6')]
        rolls = ['{}{}{}{}{:0>2}'.format(y[0],c,y[1],b,n) for c in codes for b in batches for n in nums for y in years]
        urlf = "http://results.ietdavv.edu.in/DisplayStudentResult?rollno={}&typeOfStudent=Regular"
        for roll in rolls:
            url = urlf.format(roll)
            yield scrapy.Request(url=url, callback=self.parseGradesheet)

    def clean(self, s):
        # cleaning the page

    def parseGradesheet(self, response):
        page = response.url
        if True:

        else:
            self.log('Wierd site %s', response.url)
