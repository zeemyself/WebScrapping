import urllib2
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
        return ["0","0"]
    arr = []
    # f = open('D:/Senior Project/web scrapping/text.txt','w')
    try:
        url = urllib2.urlopen(url).read()
        url = strip_tags(url)
        # f.write(url)
        soup = BeautifulSoup(url,'lxml')
        times = 0
        for link in soup.find_all("span",class_="_c24"):
            h = link.contents
            # print h
            # f.write(str(h))
            if times > 0:
             arr.append(h)
            # print h
            times +=1
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

s2n = getlink("http://www.siam2nite.com/")
# Only event not ads or other useless link
data = []
onlyevent = event(s2n)

for link in onlyevent:
    data.append(getDataFB(getFB(link)))
print data


for x in data:
   if len(x) >0:
    print "TEL:"
    print x[0]
    print "\n";
    print "EMAIL:"
    print x[1]
    print "\n";
