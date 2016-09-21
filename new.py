
import string
import datetime

def readFileToArray( filename ):
    arr = [] # list of rankings
    with open( filename ) as file:
        for line in file:
            tmp = line.strip(string.whitespace)
            arr.append(int(tmp))
    file.close()
    return arr

def naiveAlgo( arr ):
    length = len(arr)
    inversion = 0
    # naive search
    for i in range(0, length,1):
        for j in range(i+1, length,1):
            if  arr[i] > 2 * arr[j]:
                    inversion = inversion + 1
    return inversion

if __name__ == '__main__':
    a = readFileToArray( 'hw1test.txt')
    print datetime.datetime.now()
    inv = naiveAlgo(a)
    print inv
    print datetime.datetime.now()


