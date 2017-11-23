import requests
import datetime
from dateutil.relativedelta import relativedelta


def request(url, timestamp):
    payload = {'url': url, 'timestamp': timestamp}
    r = requests.get('https://archive.org/wayback/available', params=payload)
    print(r.text)


url = input("URL: ")

date = datetime.date(1996, 1, 1)

for i in range(45):
    datestr = str(date)
    print(request(url, datestr.replace('-', '')))
    date += relativedelta(months=6)
