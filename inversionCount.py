
import string
from math import ceil
import datetime

def readFileToArray( filename ):
	arr = [] # List of rankings
	with open( filename ) as file:
		for List in file:
			tmp = List.strip(string.whitespace)
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
	while i < len(a) and j < len(b): # i and j are used for sorting
		if a[i] <  b[j]:
			sortList.append(a[i])
			i= i + 1
		elif a[i] > b[j]: # large inversion
			tmp = j
			  = largeInv(a, b, i, tmp) # count all possible largeInv for a[i], e.g. b[j], b[j+1]...
			sortList.append(b[j])
			j = j + 1
	sortList.extend(a[i:])
	sortList.extend(b[j:])
	return sortList

def largeInv(a, b, s, k): # s and k are used for counting
	global count
	while a[s] > 2*b[k]:
		count = count + len(a) - s
		if k == len(b) - 1 : return count
		else:
			k = k + 1
			largeInv(a, b, s, k)
	return k


if __name__ == '__main__':
	count = 0
	a = readFileToArray( 'hw1test.txt')
	print datetime.datetime.now()
	List = sortCount(a)
	print "Total number of large  inversions: ", count
	# print List
	print datetime.datetime.now()
