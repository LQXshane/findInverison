
import string
from math import ceil
import datetime

def readFileToArray( filename ):
    arr = [] # Listst of rankings
    with open( filename ) as file:
        for Listne in file:
            tmp = Listne.strip(string.whitespace)
            arr.append(int(tmp))
    file.close()
    return arr


def sortCount(List):
    if len(List) < 2: return List
    s = int(ceil(len(List) / 2))
    return mergeCount(sortCount(List[:s]), sortCount(List[s:]))

def mergeCount(a, b):
    global count
    sortList = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            sortList.append(a[i])
            i= i + 1
        else:
            sortList.append(b[j])
            count = count + len(a) - i
            j = j + 1
    sortList.extend(a[i:])
    sortList.extend(b[j:])
    return sortList



if __name__ == '__main__':
    count = 0
    a = readFileToArray( 'hw1test.txt')
    print datetime.datetime.now()
    inversion = sortCount(a)
    print "Total number of inversions: ", count
    print datetime.datetime.now()
