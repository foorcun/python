import urllib.request
from bs4 import BeautifulSoup


url = "https://www.youtube.com/playlist?list=PLbu98QxRH81K51RxS6kCVYjmgmIdZoUU2"

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
##print(soup.prettify())
title = soup.title.get_text()
print(title)
print('##############')

list= soup.find_all('table',{'id':'pl-video-table'})

soup_list = list_corba_yap(list)

a_lar = soup_list.find_all('a')

#for y in a_lar:
 #   print(y.get_text())


fle = open('C:\\Users\\furkanselma\\Desktop\\asdf.html' , 'w',encoding='utf-8')


fle.write(title)
fle.write("###########")


a=0
for i in a_lar:

    if a%3==1:
        print(i.get_text())
        i = str(i)
        fle.write(i)
        fle.write("<br>")
    else:
        print("")
    a= a+1


fle.close()



#<table id="pl-video-table" class="pl-video-table">
