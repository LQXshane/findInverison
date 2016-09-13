# qiuxuan.lin

import string


text = []
with open('hw1test.txt') as file:
    for line in file:
        tmp = line.strip(string.whitespace)
        text.append(int(tmp))




