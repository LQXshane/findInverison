# qiuxuan.lin

import string
from math import ceil

def readFileToArray( filename ):
    arr = [] # list of rankings
    with open( filename ) as file:
        for line in file:
            tmp = line.strip(string.whitespace)
            arr.append(int(tmp))
    file.close()
    return arr

def sortCount(List):
    n = len(List)
    r = 0
    if n == 0:
        return r # return 0 if there is no list
    else:
        A = List[0: (ceil(n/2)-1) ]
        B = List[ceil(n/2): n]
        r1, A = sortCount(A)
        r2, B = sortCount(B)
        r, L = mergeCount(A,B)
    r = r1 + r2 + r
    return r, L

def mergeCount(a, b):
    i = 0
    j = 0
    count = 0
    l = [] # init
    while len(a) != 0 and len(b) != 0:
        l.append(min(a[i], b[j]))
        if b[j] < a[i]:
            count = count + len(a) - i
            j = j + 1
        else:
            i = i + 1
    while len(a) == 0 or len(b) == 0:
        if len(a) == 0:
            l.append(b)
        else:
            l.append(a)

    return count, l

