import re

from selenium import webdriver

driver = webdriver.Chrome("C:/Users/furkanselma/Documents/python/selenium kutuphanesi/install/chromedriver.exe")

driver.get("https://www.google.com.tr")


try:
  driver.find_element_by_id('gbw')
  print('Test pass: ID found')


except Exception as e:
  print('Exception found' , format(e))
  



driver.quit()
