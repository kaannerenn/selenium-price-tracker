from .base_scraper import BaseScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AmazonScraper(BaseScraper):
    
    def __init__(self):
        super().__init__()
        self.base_url = "https://www.amazon.com.tr"

    def search_product(self,keyword):
        self.navigate(self.base_url)
        
        self.wait_for_element_visibility(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div[1]/input")

        search_input = self.driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div[1]/input")
        search_input.click()
        search_input.send_keys(keyword + Keys.ENTER)

    def _get_price(self,card):
        try:
            product_price = card.find_element(By.CLASS_NAME,"a-price-whole").text
            return product_price
        except:
            return "Fiyat bulunamadı"
        
    def _get_img(self,card):
        try:
            product_img = card.find_element(By.TAG_NAME, "img")
            return product_img.get_attribute("src")
        except:
            return "Resim bulunamadı"
        
    def _get_link(self, card):
        try:
            link_element = card.find_element(By.TAG_NAME, "a")
            return link_element.get_attribute("href")
        except:
            try:
                link = card.get_attribute("href")
                return link if link else "Link bulunamadı"
            except:
                return "Link bulunamadı"
            
    def get_products(self):
        self.wait_for_element_visibility(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
        cards = self.driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
        scraped_data = []

        for card in cards:
            try:
                product_name = card.find_element(By.TAG_NAME, "h2").text.strip()
                product_price = self._get_price(card)
                product_img = self._get_img(card)
                product_link = self._get_link(card)

                item = {
                    "name":product_name,
                    "price":product_price,
                    "img": product_img,
                    "link":product_link
                }
                scraped_data.append(item)
            except Exception as e:
                continue
        
        return scraped_data
                