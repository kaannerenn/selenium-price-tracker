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

def get_card(driver):
    return driver.find_elements(By.CLASS_NAME,"product-card")
def get_price(card):
    possible_classes = ["price-section","sale-price","price-value"]

    for class_name in possible_classes:
        try:
            product_price = card.find_element(By.CLASS_NAME,class_name).text
            return product_price
        except:
            continue
    return "Fiyat bulunamadı."
def get_image(card):
    try:
        product_img = card.find_element(By.TAG_NAME, "img")
        return product_img.get_attribute("src")
    except:
        return "Resim bulunamadı"
def get_link(card):
    try:
        return card.get_attribute("href")
    except:
        return "Link bulunamadı"


product_cards = get_card(driver)

print(len(product_cards))
for card in product_cards:
    try:
        product_name = card.find_element(By.CLASS_NAME,"title")
        product_price = get_price(card)
        product_img = get_image(card)
        product_link = get_link(card)
        print(f"Ürün: {product_name.text} | Fiyat: {product_price} | Resim link: {product_img} | Ürün link:{product_link} ")
    except Exception as e:
        continue



input("Enter Bas (Çıkış için)")
driver.quit()