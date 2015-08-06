import urllib2
import MySQLdb
from bs4 import BeautifulSoup
# Print all email if its found from target URL
# @url : Target url ex. "http://www.siam2nite.com"
# Return all link from target url in array
def getlink(url):
    arr = []
    try:
        soup = BeautifulSoup(urllib2.urlopen(url).read(),"lxml")
        for link in soup.find_all('a'):
        #  print link.get('href')
         arr.append(link.get('href'))
    except Exception as e:
        print "Internet Error \nCause : " + str(e)
    return arr
# Remove Comment ** Facebook formate issue
def strip_tags(string):
    x = string.replace("<!--","")
    return x.replace("-->","")

# Show information of target event
# @url Event facebook URL
# Return array of data array(Name,Phone Number,EMAIL) not in format
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
        if len(arr) == 1:
            arr.append("No")
            arr.append("No")
    except Exception as e:
        print "Internet Error \nCause : " + str(e)
    return arr

def event(arr):
    ret = []
    for x in arr:
        if x is not None:
         if x[:35] == "http://www.siam2nite.com/en/events/":
          ret.append(x)
    return ret

def getFB(url):
    arr=[]
    try:
        soup = BeautifulSoup(urllib2.urlopen(url).read(),"lxml")
        for link in soup.find_all('a'):
          arr.append(link.get('href'))
    except Exception as e:
        print "Internet Error \nCause : " + str(e)
    for s in arr:
     if s is not None:
      if s[:24] == "https://www.facebook.com":
       return s
    return 0
def remove_duplicates(l):
    return list(set(l))
s2n = getlink("http://www.siam2nite.com/en/events")
# Only event not ads or other useless link
data = []
onlyevent = event(s2n)
f = open('D:/Senior Project/web scrapping/6-8-2015.txt','w')
onlyevent = remove_duplicates(onlyevent)
print onlyevent
for link in onlyevent:
    data.append(getDataFB(getFB(link)))
    # f.write(link + "\n")

# data.append(getDataFB(getFB('http://www.siam2nite.com/en/events/2015-07-29/3rd-anniversary-7026')))
# data.append(getDataFB(getFB('http://www.siam2nite.com/en/events/2015-08-01/introducing-52hz-7229')))
# print data
# print data[0][0]
# print data[0][1]
# print data[0][2]
def tel(string):
    if (len(string) > 2):
     return string[3:-2]
    return "No"
def mail(string):
    if (len(string) > 2):
        return string.split('>')[1].split('<')[0]
    return "No"
def que(string):
    return string.replace("'","''")
print data
print "-------------------------------------------------------"
for x in data:
   if len(x) >0:
    print "TITLE:" + x[0].encode("utf-8")
    f.write("\nTITLE:" + x[0].encode("utf-8"))
    print "TEL:" + tel(str(x[1]))
    f.write("\nTEL:" + tel(str(x[1])))
    # print "TEL:" + str(x[0]).split("'")[1].split("'")[0]
    print "EMAIL:" + mail(str(x[2]))
    f.write("\nEMAIL:" + mail(str(x[2])))
    # print "EMAIL:" + str(x[1]).split('>')[1].split('<')[0]





db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="", # your password
                      db="creatordatabase") # name of the data base
cur = db.cursor()

for x in data:
    if len(x) > 0 :
        title = que(x[0].encode("utf-8"))
        teln = tel(str(x[1]))
        email = mail(str(x[2]))

        cur.execute("INSERT INTO creator(Title,Tel,Email) VALUES ('%s','%s','%s')" % (title,teln,email))
        db.commit()
