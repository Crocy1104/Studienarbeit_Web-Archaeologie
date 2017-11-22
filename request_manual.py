import requests


def request(url, timestamp):
    payload = {'url': url, 'timestamp': timestamp}
    r = requests.get('https://archive.org/wayback/available', params=payload)
    print(r.text)


url = input("URL: ")
timestamp = input("Timestamp: ")

request(url, timestamp)

