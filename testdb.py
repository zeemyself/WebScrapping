import MySQLdb
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="", # your password
                      db="creatordatabase") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
# cur.execute("SELECT * FROM creator")
#
# # print all the first cell of all the rows
# for row in cur.fetchall() :
#     print row
tt = "etstesn"
t = "09 32424 234"
em = "zeexmint@love.com"
if cur.execute("INSERT INTO creator(Title,Tel,Email) VALUES ('%s','%s','%s')" % (tt,t,em)):
    print "Done"
db.commit()
