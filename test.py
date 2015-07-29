import urllib2
from bs4 import BeautifulSoup
def geturl(url):
    import urllib2
    from bs4 import BeautifulSoup
    arr = []
    try:
        soup = BeautifulSoup(urllib2.urlopen(url).read(),"lxml")
        for link in soup.find_all('a'):
        #  print link.get('href')
         arr.append(link.get('href'))
    except Exception as e:
        print "Internet Error \nCause : " + str(e)

    print arr
    for s in arr:
     if s is not None:
      if s[:7] == "mailto:":
       print s

# web = input('Enter Website:');
arr = []
try:
    soup = BeautifulSoup(urllib2.urlopen('http://www.siam2nite.com/en/events/2015-07-24/cocktails-at-nine-7141').read(),"lxml")
    for link in soup.find_all('a'):
    #  print link.get('href')
    #  if (link.get('href').string) is not None:
      arr.append(link.get('href'))
except Exception as e:
    print "Internet Error \nCause : " + str(e)

# prinst arr

for s in arr:
 if s is not None:
  if s[:24] == "https://www.facebook.com":
   print s
   geturl(s)
