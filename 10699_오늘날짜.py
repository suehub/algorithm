import datetime as dt

datetTime = str(dt.datetime.now()).split(' ')
year = datetTime[0].split('-')

print('{0}-{1}-{2}'.format(year[0], year[1], year[2]))