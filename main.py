from scrapers.trendyol_scraper import TrendyolScraper
import json

def main():
    bot = TrendyolScraper()
    bot.search_product("Acer Bilgisayar")
    data = bot.get_products()

    with open("products.json",'w',encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    bot.close()

if __name__ == "__main__":
    main()