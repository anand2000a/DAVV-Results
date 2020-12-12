import scrapy
import json
import os


class IETDAVVGradeSpider(scrapy.Spider):
    name = "Gradesheet"

    def start_requests(self):
        # enter the build url here
        # CVIETM
        codes = ['E']
        batches = ['0']
        nums = [i for i in (range(50, 70))]
        years = [('19', '2'), ('18', '4'), ('17', '6'), ('16', '8')]
        rolls = ['{}{}{}{}{:0>2}'.format(
            y[0], c, y[1], b, n) for c in codes for b in batches for n in nums for y in years]
        header = {'user-agent': 'yaaar-le-lene-do-yaar-data/4.0.4'}
        urlf = "http://results.ietdavv.edu.in/DisplayStudentResult?rollno={}&typeOfStudent=Regular"
        for roll in rolls:
            url = urlf.format(roll)
            yield scrapy.Request(url=url, headers=header, callback=self.parseGradesheet)

    def parseGradesheet(self, response):
        if(response.status == 500 or response.status == 404):
            return

        if(response.css("h1::text").extract() == "ROLL NUMBER NOT FOUND."):
            print(response.css("h1::text").extract())
            return
        if(response.css("h2::text").extract() == "The page you are looking for can't be found."):
            print(response.css("h1::text").extract())
            return
        data = {}
        data['Title'] = response.css("font::text")[2].extract()
        tables = response.css("table")
        tables = tables.css("table")

        # extract student info
        heads = tables[3].css("font::text").getall()
        vals = tables[3].css("b::text").getall()
        data['Info'] = {heads[i]: vals[i] for i in range(len(vals))}

        # extract grades
        grades = []
        heads = tables[4].css("th").css("font::text").getall()
        subjects_and_codes = tables[4].css("tr").css(
            "td").css("font::text").getall()
        total_subjects = len(subjects_and_codes)
        score = tables[4].css("tr").css("td").css("b::text").getall()
        for i in range(1, total_subjects):
            course = {heads[0]: subjects_and_codes[i-1], heads[1]: subjects_and_codes[i], heads[2]: score[i-1], heads[3]: score[i], }
            i = i+1
            grades.append(course)
        data['Grades'] = grades

        # get result
        heads = tables[5].css("b::text").getall()
        result = {'Status': heads[0], 'SGPA': heads[1]}
        data['Result'] = result

        filename = data["Info"]["Roll Number"]+'.json'
        filepath = os.path.join('data', filename)
        with open(filepath, 'w') as json_file:
            json.dump(data, json_file, indent=4)
