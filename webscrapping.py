import requests
from bs4 import BeautifulSoup
import pandas as pd
# url = "https://www.amazon.in/s?k=iphone"
# url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
url = "https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/"
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html')
print(soup)
# print("hi")

# data = {'title': [], 'price': []}

# print(span)
# for item in span_title:
#     print(item.string)
# span_price = soup.select("span.a-price-whole")
# span_titles = soup.select("span.a-size-medium.a-color-base.a-text-normal")
# for item in span_titles:
#     print(item.string)

# print(len(span_titles))
# for i in range(len(span_titles)):
#     a = {span_titles[i].string: span_price[i].string}
#     print(a)



# for item in span_price:
#     data["title"].append(item.string)

# for item in span_titles:
#     data["price"].append(item.string)

# df = pd.DataFrame.from_dict(data)
# df.to_csv("data.csv", index=False)
# print(span_price)

