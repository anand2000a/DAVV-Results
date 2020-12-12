import scrapy
import json
import os


class IETDAVVGradeSpider(scrapy.Spider):
    name = "Gradesheet"

    def start_requests(self):
        # enter the build url here
        codes = ['C', 'V', 'I', 'E', 'T', 'M']
        batches = ['0', '1']
        nums = [i for i in range(1, 100)]
        years = [('19', '2'), ('18', '4'), ('17', '6')]
        rolls = ['{}{}{}{}{:0>2}'.format(
            y[0], c, y[1], b, n) for c in codes for b in batches for n in nums for y in years]
        urlf = "http://results.ietdavv.edu.in/DisplayStudentResult?rollno={}&typeOfStudent=Regular"
        for roll in rolls:
            url = urlf.format(roll)
            yield scrapy.Request(url=url, callback=self.parseGradesheet)

    def parseGradesheet(self, response):
        page = response.url
        data = {}
        data['Title'] = page.css("font::text")[2].extract()
        tables = response.css("table")
        tables = tables.css("table")

        # extract student info
        heads = tables[3].css("font::text").getall()
        vals = tables[3].css("b::text").getall()
        data['Info'] = {heads[i]: vals[i] for i in range(len(vals))}
        # print(data['Info'])

        # extract grades
        heads = tables[4].css("th").css("font::text").getall()
        data['Grades'] = {heads[i]: vals[i] for i in range(len(vals))}
        # print(heads)
        filename = 'Gradesheet.json'
        filepath = os.path.join('data', filename)
        with open(filepath, 'w') as json_file:
            json.dump(data, json_file, indent=4)
