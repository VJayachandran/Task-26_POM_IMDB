"""
POM - Code without implementing Page Object Model
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# For Fluent wait only
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementClickInterceptedException

class Jai:

   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   ignored_exceptions = [NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException]
   wait = WebDriverWait(driver, 10, poll_frequency=5, ignored_exceptions=ignored_exceptions)

   def __init__(self, web_url):
       self.url = web_url

   def login(self):
       try:
           self.driver.maximize_window()
           self.driver.get(self.url)
           username = self.wait.until(EC.presence_of_element_located((By.NAME, "username12345")))
           password = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
           submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
           username.send_keys("Admin")
           password.send_keys("admin123")
           submit_button.click()
       except (NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException) as e:
           print(e)
       finally:
           self.driver.quit()

if __name__ == "__main__":
   url = "https://www.imdb.com/search/name/"
   jai1 = Jai(url)
   jai1.login()