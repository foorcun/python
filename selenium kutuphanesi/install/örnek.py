import time

from selenium import webdriver

driver = webdriver.Chrome("C:/Users/furkanselma/Documents/python/selenium kutuphanesi/install/chromedriver.exe")

driver.get("https://eksisozluk.com")

print(driver.title)

time.sleep(8)
driver.quit()
