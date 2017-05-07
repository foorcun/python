import urllib.request
from bs4 import BeautifulSoup
import webbrowser


url = "https://www.youtube.com/playlist?list=PLbu98QxRH81K51RxS6kCVYjmgmIdZoUU2"

#url = "http://www.pornhub.com/"


def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


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
#<table id="pl-video-table" class="pl-video-table">


soup_list = list_corba_yap(list)

a_lar = soup_list.find_all('a')

#for y in a_lar:
 #   print(y.get_text())





b=0
no=1
vid_adlar=[]
for i in a_lar:   ##video adlarını yazar

    if b%3==1:
        vid_adlar.append(i.get_text())
        print(str(no) + i.get_text())
        no=no+1
        
    else:
        print("")
    b= b+1




vid_linkler=[]    ###linkleri bu diziye diziyor ve ekrana yazıdırıyor
for a in soup_list.find_all('a', href=True):  
  if b%3==1:
    vid_linkler.append("http://tr.keepvid.com/?url=https://www.youtube.com" + a['href'])
    print ("Found the URL:", a['href'])

  b=b+1




for link in vid_linkler:
    

    webbrowser.open_new(link)

    input('sonraki için bır tusa basın')

print('BİTTİ')

###  keepvid kısmı





#################bu kısım otomatık ındırme kodları olcak
  
#new_url=vid_linkler[0]
#sauce_keep = sos_al(new_url)
#soup_keep = corba_yap(sauce_keep)



#keep_div=soup_keep.find_all("div",{'class':'d-info2'})
#print(keep_div)


#soup_keep2=list_corba_yap(keep_div)
#a_keep = soup_list.find_all('a',href=True)








