from scrapers.trendyol_scraper import TrendyolScraper
from scrapers.amazon_scraper import AmazonScraper
import json
from utils import save_to_json

def main():
    bot = TrendyolScraper()
    bot.search_product("Acer Bilgisayar")
    data = bot.get_products()

    if data:
        save_to_json(data, filename="trendyol_products.json")
    else:
        print("Veri yok.")
    bot.close()
    
    bot = AmazonScraper()
    bot.search_product("Acer Bilgisayar")
    data = bot.get_products()
    if data:
        save_to_json(data, filename="amazon_products.json")
    else:
        print("Veri yok.")
    bot.close()
    
if __name__ == "__main__":
    main()