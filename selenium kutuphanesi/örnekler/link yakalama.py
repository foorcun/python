import re
import linkGrabber
##link grabberı yuklemke için
##   pip install linkGrabber

links = linkGrabber.Links('http://google.com')

gb=links.find(limit=4,dublicates= False, pretty=True)

print(gb)
