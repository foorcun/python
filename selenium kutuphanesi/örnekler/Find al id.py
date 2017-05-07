import re

from selenium import webdriver

driver = webdriver.Chrome("C:/Users/furkanselma/Documents/python/selenium kutuphanesi/install/chromedriver.exe")

driver.get("https://www.google.com.tr")



ids = driver.find_elements_by_xpath('//*[@id]')


for ii in ids:
  print(ii.get_attribute('id'))

  



driver.quit()
