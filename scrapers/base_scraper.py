from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BaseScraper:
    def __init__(self, timeout=10):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver,timeout)

    def navigate(self,url):
        self.driver.get(url)

    def wait_for_element_visibility(self, by, value_str):
        return self.wait.until(expected_conditions.visibility_of_element_located((by, value_str)))
    
    def close(self):
        self.driver.quit()