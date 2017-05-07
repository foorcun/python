import time
import re

from selenium import webdriver

driver = webdriver.Chrome("C:/Users/furkanselma/Documents/python/selenium kutuphanesi/install/chromedriver.exe")

driver.get("http://www.international.itu.edu.tr/Icerik.aspx?sid=1067")


doc =driver.page_source

emails = re.findall(r'[\w\.-]+@[\w\.-]+',doc)

for email in emails:
  print(email)


driver.quit()
