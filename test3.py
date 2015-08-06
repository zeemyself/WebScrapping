import re



errorx = "u'081 943 1732'"
def strip_tags(string):
    x = string.replace("<!--","")
    return x.replace("-->","")
ad =  str(errorx)[2:-1]
print ad
# print strip_tags(errorx)

# print errorx.split('>')[1].split('<')[0]

# xd = "455353453"
# print xd[100:]
#
# arr = [["wawfawfafafawfw","u'0846607193","zeemyself@gmail.com"],["0","0","0"],["0","0","0"],["0","0","0"],[]]
#
# for x in arr:
#     print len(x)
#     print x[1][3:]
# # print arrayxx()
