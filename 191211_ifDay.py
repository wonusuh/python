import datetime
dt = datetime.datetime.now() #날짜 객체
wd = dt.weekday()
wday = ''

if wd == 0:
    wday = '월'
elif wd == 1:
    wday = '화'
elif wd == 2:
    wday = '수'
elif wd == 3:
    wday = '목'
elif wd == 4:
    wday = '금'
elif wd == 5:
    wday = '토'
elif wd == 6:
    wday = '일'

print('오늘은 %s요일 입니다.' %wday)
