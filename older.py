import urllib.request


def printresult(rollNO):
    filename = str(rollNO[45:])
    f = open(filename+".html", 'w')
    response = urllib.request.urlopen(rollNO)
    webContent = response.read()
    f.write(str(webContent))
    f.close


cls_code = input()
n = 'http://www.ietdavv.edu.in:8080/logic2?rollno=1'


#
if cls_code == 'CSA':
    cls_rcode = n+'C20'
elif cls_code == 'CSB':
    cls_rcode == n+'C21'
elif cls_code == 'ITA':
    cls_rcode == n+'I20'
elif cls_code == 'ITB':
    cls_rcode == n+'I21'
elif cls_code == 'CIVIL':
    cls_rcode == n+'V30'
elif cls_code == 'ECI':
    cls_rcode == n+'E20'
elif cls_code == 'ECTA':
    cls_rcode == n+'T20'
elif cls_code == 'ECTB':
    cls_rcode == n+'T21'
elif cls_code == 'MECH':
    cls_rcode == n+'M20'

for i in range(1, 10):
    rollNO = cls_rcode+'0'+str(i)
    printresult(rollNO)

for i in range(10, 99):
    rollNO = cls_rcode+str(i)
    printresult(rollNO)
