import urllib.request
from bs4 import BeautifulSoup
import re

url = "http://www.sks.itu.edu.tr/" 
#url = "http://www.opensubtitles.org/tr"


sauce = urllib.request.urlopen(url).read()#url sources alınır
soup = BeautifulSoup(sauce,"html.parser")#corbası yapılır

#print(soup.prettify())


#divs=soup.find_all("div") # bunun sonucu list seklınde geliyor



print(soup('h2',{'title':'Yemek Menusu'})[0].string,'\n')### cok guzel text alma yontemı  ## tarih kısmını cektı
##<h2 title="Yemek Menusu">Günün Yemek Menüsü - 09 Aralık 2016</h2>



#print(soup.find(id='cphHaberDuyuru_C015_Col00'))    #istedigimiz divi aldık

div_ogle= soup.find(id='cphHaberDuyuru_C015_Col00')
div_ogle=str(div_ogle)
div_ogle= BeautifulSoup(div_ogle,'html.parser')

yem_list = div_ogle.find_all('li',{'style':'text-align: center;'})

#a= div_ogle('li',{'style':'text-align: center;'})[0].string
#print(a)

#yem_list = str(yem_list)
#yem_list = BeautifulSoup(yem_list,'html.parser')
#yem_list = yem_list.get_text()

#div_ogle=div_ogle.prettify()
#div_ogle=str(div_ogle)
#div_ogle= BeautifulSoup(div_ogle,'html.parser')
#div_ogle= div_ogle.get_text()



for y in yem_list:
    print(y.get_text())





#den_list = soup('h2',{'style':'text-align: center; font-size: 21px;'})### cok guzel text alma yontemı

#<h2 style="text-align: center; font-size: 21px;">Öğle Yemeği</h2>

#yem_list = div_ogle('li',{'style':'text-align: center;'})
#<li style="text-align: center;">Erzincan Çorbası</li>


#for a in yem_list:
 #   print(a)
'''
for a in den_list:
    print(a)
'''






'''for eachD in divs:
    
    each = str(eachD)
    a=re.search("ogle-yemegi",each)


    if a== None:
        a=a
    else:
        a=BeautifulSoup(each,"html.parser")
        a=a.prettify()
        
        a= BeautifulSoup(a,"html.parser")
        
        a=a.get_text()
        ogle_yem.append(a)
        
'''



#print(ogle_yem[1])

b=input("haydi söyle ")

    



#divs=str(divs) # soup ancak str seklındeyse yapılabılıyor list te olmuyor
#divs_soup= BeautifulSoup(divs,"html.parser")
#print(divs_soup.get_text())






