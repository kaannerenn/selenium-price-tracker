from .base_scraper import BaseScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TrendyolScraper(BaseScraper):

    def __init__(self):
        super().__init__()
        self.base_url = "https://www.trendyol.com"

    def search_product(self, keyword):
        self.navigate(self.base_url)
        #/html/body/div[2]/div/div/div[2]/img
        #/html/body/div[1]/div/div/div[2]
        self.wait_for_element_visibility(By.XPATH,"/html/body/div[2]/div/div/div[2]")

        self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]").click()

        self.wait_for_element_visibility(By.XPATH,"/html/body/header/div[2]/div/div[2]/div/div[2]/div[1]/button[2]")

        self.driver.find_element(By.XPATH,"/html/body/header/div[2]/div/div[2]/div/div[2]/div[1]/button[2]").click()

        self.wait_for_element_visibility(By.NAME,"search-input")

        self.driver.find_element(By.NAME,"search-input").send_keys(keyword + Keys.ENTER)
    
    def _get_price(self,card):
            possible_classes = ["price-section","sale-price","price-value"]

            for class_name in possible_classes:
                try:
                    product_price = card.find_element(By.CLASS_NAME,class_name).text
                    return product_price
                except:
                    continue
            return "Fiyat bulunamadı."

    def _get_img(self,card):
                try:
                    product_img = card.find_element(By.TAG_NAME, "img")
                    return product_img.get_attribute("src")
                except:
                    return "Resim bulunamadı"

    def _get_link(self,card):
            try:
                return card.get_attribute("href")
            except:
                return "Link bulunamadı"


    def get_products(self):
        self.wait_for_element_visibility(By.CLASS_NAME,"search-result-content")
        cards = self.driver.find_elements(By.CLASS_NAME, "product-card")

        scraped_data = []

        for card in cards:
            try:
                product_name = card.find_element(By.CLASS_NAME,"title").text
                product_price = self._get_price(card)
                product_img = self._get_img(card)
                product_link = self._get_link(card)
                
                item = {
                     "name": product_name,
                     "price": product_price,
                     "image": product_img,
                     "link": product_link
                }
                scraped_data.append(item)
                print(f"Ürün:{product_name}, Fiyat: {product_price}, image link: {product_img}, product link: {product_link}")
            except Exception as e:
                continue

        return scraped_data
