import requests

url = "https://timesofindia.indiatimes.com/"
r = requests.get(url)
print(r.text)