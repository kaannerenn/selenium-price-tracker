from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

TIMEOUT = 10

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.trendyol.com")

WebDriverWait(driver,TIMEOUT).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[2]")))
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]").click()
WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/header/div[2]/div/div[2]/div/div[2]/div[1]/button[2]")))
search_bar_trendyol = driver.find_element(By.XPATH,"/html/body/header/div[2]/div/div[2]/div/div[2]/div[1]/button[2]")
search_bar_trendyol.click()
WebDriverWait(driver,TIMEOUT).until(expected_conditions.visibility_of_element_located((By.NAME,"search-input")))
search_bar_trendyol_2 = driver.find_element(By.NAME,"search-input")
search_bar_trendyol_2.send_keys("Acer Bilgisayar")
search_bar_trendyol_2.send_keys(Keys.ENTER)
WebDriverWait(driver,TIMEOUT).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"search-result-content")))

'''product_names = driver.find_elements(By.CLASS_NAME,"title")
del product_names[0]
print(len(product_names))
for i in product_names:
    print(i.text)
product_prices = driver.find_elements(By.CLASS_NAME,"price-section")
print(len(product_prices))
for i in product_prices:
    print(i.text)
'''
product_cards = driver.find_elements(By.CLASS_NAME,"product-card")
print(len(product_cards))
for card in product_cards:
    try:
        product_name = card.find_element(By.CLASS_NAME,"title")
        try:
            product_price = card.find_element(By.CLASS_NAME,"price-section")
        except:
            try:
                product_price = card.find_element(By.CLASS_NAME,"sale-price")
            except:
                product_price = card.find_element(By.CLASS_NAME,"price-value")
        print(f"Ürün: {product_name.text} | Fiyat: {product_price.text}")
    except:
        continue
input("Enter Bas")
driver.quit()