import urllib2
import re, copy
from bs4 import BeautifulSoup
# Used for Facebook cuz facebook comment code
def strip_tags(string):
    x = string.replace("<!--","")
    return x.replace("-->","")


def getDataFB(url):

arr = []
f = open('D:/Senior Project/web scrapping/text.txt','w')
try:
    url = urllib2.urlopen(url).read()
    url = strip_tags(url)
    # f.write(url)
    soup = BeautifulSoup(url,'lxml')

    for link in soup.find_all("span",class_="_c24"):
        h = link.contents
        # print h
        f.write(str(h))
        arr.append(h)
        print h
except Exception as e:
    print "Internet Error \nCause : " + str(e)
