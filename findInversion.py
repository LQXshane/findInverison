# qiuxuan.lin

import string
import datetime

a = [] # list of rankings
with open('hw1test.txt') as file:
    for line in file:
        tmp = line.strip(string.whitespace)
        a.append(int(tmp))

n = len(a)
inversion = 0 # of large inversions

print datetime.datetime.now()
# naive search
for i in range(0,n,1):
    for j in range(0,n,1):
        if i < j:
            if a[i]>2 * a[j] :
                inversion = inversion + 1

print datetime.datetime.now()







