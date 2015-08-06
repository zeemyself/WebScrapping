import urllib2
import re, copy
from bs4 import BeautifulSoup
# Used for Facebook cuz facebook comment code
def strip_tags(string):
    x = string.replace("<!--","")
    return x.replace("-->","")


def getDataFB(url):
    if url ==0:
        return ["0","0","0"]
    arr = []
    # f = open('D:/Senior Project/web scrapping/text.txt','w')
    try:
        url = urllib2.urlopen(url).read()
        url = strip_tags(url)
        # f.write(url)
        soup = BeautifulSoup(url,'lxml')
        times = 0
        arr.append(soup.title.string)
        for link in soup.find_all("span",class_="_c24"):
            h = link.contents
            # print h
            # f.write(str(h))
            if times >0:
             arr.append(h)
            # print h
            times +=1
        print(len(arr))
    except Exception as e:
        print "Internet Error \nCause : " + str(e)
    return arr



# xx =  getDataFB('https://www.facebook.com/events/1659560534263366/')
# print xx
# print xx[0].encode("utf-8")

prob = "INTUS Launch Party! Germany's Biggest DJ's @LIVE RCA + After Party @Secret Location | Facebook"
prob = prob.replace("'","''")
import MySQLdb
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="", # your password
                      db="creatordatabase") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

cur.execute("INSERT INTO creator(Title,Tel,Email) VALUES ('%s','%s','%s')" % (prob,"TEST","TEST"))







db.commit()
