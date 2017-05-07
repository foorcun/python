#!\Users\furkanselma\AppData\Local\Programs\Python35-32

import urllib.request
from bs4 import BeautifulSoup


url = "http://www.sks.itu.edu.tr/"

#url = "http://www.pornhub.com/"



def sos_al(url):

    sauce = urllib.request.urlopen(url).read()#url source code alınır
    return sauce


def corba_yap(sauce):
    
    soup = BeautifulSoup(sauce,"html.parser")#corbası yapılır
    return soup


def list_corba_yap(lst):
    lst=str(lst)
    lst=BeautifulSoup(lst,'html.parser')
    return lst

sauce = sos_al(url)


soup = corba_yap(sauce)
asdf=soup('h2',{'title':'Yemek Menusu'})
if len(asdf)>0:
    print(asdf[0].string,'\n')### cok guzel text alma yontemı  ## tarih kısmını cektı
elif len(asdf)==0:
    print('yemek bulamadık hacı')
##<h2 title="Yemek Menusu">Günün Yemek Menüsü - 09 Aralık 2016</h2>


div_ogle= soup.find(id='cphHaberDuyuru_C015_Col00') #istedigimiz divi aldık

div_ogle = list_corba_yap(div_ogle)

yem_list = div_ogle.find_all('li',{'style':'text-align: center;'})

print('Öğle yemeği','\n')
for y in yem_list: ###cok onemlı bir kullanım
    print(y.get_text())# get_text() fonksiyonu normalde listelerde kullanılmıyor
                        # ama boyle dongu yapınca kullanılabılıyr

print('\n')

print('Akşam yemeği','\n')


div_ogle= soup.find(id='cphHaberDuyuru_C015_Col01') #istedigimiz divi aldık
div_ogle = list_corba_yap(div_ogle)
yem_list = div_ogle.find_all('li',{'style':'text-align: center;'})
for y in yem_list: ###cok onemlı bir kullanım
        print(y.get_text())# get_text() fonksiyonu normalde listelerde kullanılmıyor





b=input("haydi söyle ")







