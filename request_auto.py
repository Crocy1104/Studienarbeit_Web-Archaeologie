import requests
import datetime
from dateutil.relativedelta import relativedelta

date = datetime.date(1996, 1, 1)

for i in range(45):
    datestr = str(date)
    print(datestr.replace('-', ''))
    date += relativedelta(months=6)
