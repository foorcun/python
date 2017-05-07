#!/usr/bin/python3
#-*- coding: utf-8 -*-

from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

url = "https://onedio.com/haber/umberto-eco-nun-ele-aldigi-fasist-ideolojinin-olmazsa-olmaz-14-temel-ozelligi-752570"
#url="https://www.pornhub.com"
#url  = "https://www.youtube.com/watch?v=Dv15y5CgCyE&spfreload=10#t=3.251836"
#url= "https://onedio.com/haber/basaksehir-mustafa-pektemek-le-galatasaray-i-kupadan-eledi-iste-macin-sosyal-medya-yankilari-754704"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
# print(webpage)
soup0 = BeautifulSoup(webpage, "html.parser")

title = soup0.title.get_text()
print(title)


#fle = open('C:\\Users\\furkanselma\\Desktop\\onedio\\asdf.html' , 'w')

article=soup0.find_all('article')
article= str(article)
#fle.write(article)
soup = BeautifulSoup(article, "html.parser")

basliklar = soup.find_all('h1')
basciklar = soup.find_all('h2')
im=soup.find_all('img')



#filename='C:\\Users\\furkanselma\\Desktop\\onedio\\%s.html' % title
#fle = open(filename , 'w')
#fle = open('C:\\Users\\furkanselma\\Desktop\\onedio\\{0}.txt'.format(title), 'w')

fig=soup.find_all('figcaption')
yaz=soup0.find_all('div',{'itemprop':'articleBody'})

fle = open('C:\\Users\\furkanselma\\Desktop\\onedio\\asdf.html' , 'w',encoding='utf-8')
#encode codu eklendı sona

for i in basliklar:
    i = str(i)
    fle.write(i)
y=str(yaz[0])
fle.write(y)
sayi=len(basciklar)
fi=''
for i in range(sayi):
    cik = str(basciklar[i])
    img= str(im[i+2])
    if i<len(fig):
        fi=str(fig[i])
    
    fle.write(cik)
    fle.write(img)
    fle.write(fi)


fle.close()

'''fle = open('C:\\Users\\furkanselma\\Desktop\\onedio\\asdf.txt' , 'w')

for i in baslıklar:
    fle.write(i.get_text()+'\n\n\n')


for i in bascıklar:
    fle.write(i.get_text()+'\n\n')


fle.close()
'''
##webpage= BeautifulSoup.prettify(soup)
'''webpage = str(webpage)
fle = open('C:\\Users\\furkanselma\\Desktop\\onedio\\hello.txt','w')
fle.write(webpage)
fle.close()'''

b = input("haydi söyle ")
