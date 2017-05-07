from selenium import webdriver
from selenium.webdriver.common.keys import Keys


###  google ve diger korumalı siteler handshake fail veriyor
###  ama tırtolar ya da ozgurler de calısıo



driver = webdriver.Chrome("C:/Users/furkanselma/Documents/python/selenium kutuphanesi/install/chromedriver.exe")
driver.get("https://www.dogalmantarlar.com/turkiyede-yetisen-ve-yenilebilir-mantar-turleri/")

elem = driver.find_element_by_name("s")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
