import datetime
def dayofweek(date):
    month,day,year=(int(i) for i in date.split(' '))
    if year>2000 and year<3000:
        week=datetime.date(year,month,day)
        return week.strftime('%A')
date = input()
print(dayofweek(date).upper())