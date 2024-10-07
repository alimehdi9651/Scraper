import scrapy
from pathlib import Path
import pandas as pd

class FitnessSpider(scrapy.Spider):
    name = "fitness"
    allowed_domains = ["noon.com"]
    start_urls = ["https://noon.com"]
    def start_requests(self):
        urls = ["https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/",
                "https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/?limit=50&page=2&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc",
                "https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/?limit=50&page=3&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc",
                "https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/?limit=50&page=4&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

   
# we can use attrin["attribute_name"]- to get any specific attribute
    def parse(self, response):
        data = {'Title': [], 'Price':[], 'Sponsored': [], 'Discount':[], 'Link':[]}
        # page = response.url.split("/")[-2]
        # filename = f"fitness-{page}.html"
        # # Path(filename).write_bytes(response.body)
        # self.log(f"Saved file {filename}")
        cards = response.css(".productContainer")
       
        for card in cards:
            Title = card.css(".fPskJH>span>span::text").get()
            # print(Title)
            data["Title"].append(Title)

            Price = card.css(".RLMCJ>div>div>strong::text").get()
            # print(Price)
            
            data["Price"].append(Price)
            Sponsore = card.css(".AkmCS::text").get()
            if Sponsore:
                data["Sponsored"].append("Yes")
            else:
                data["Sponsored"].append("No")
            # for sponsore in Sponsores:
            #     if sponsore:
                    # data["Sponsored"].append("Yes")
                #     print('Yes')
                # else:
                #     print('No')
                    # data["Sponsored"].append("No")
            # print(sponsored)
            
            discount = card.css(".discount::text").get()
            
            # print(discount)
            data["Discount"].append(discount)

            # print(discount)
            # act_price = card.css(".oldPrice::text").get()
            # print(act_price)
            link = card.css(".bwele>a").attrib["href"]
            
            # print(link)
            data["Link"].append(link)
           
            
            df = pd.DataFrame.from_dict(data)
            df.to_csv("product_details.csv")
            