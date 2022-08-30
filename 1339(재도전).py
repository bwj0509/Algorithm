from re import I
import sys


import sys
from unittest import result

N = int(sys.stdin.readline())
L = []
result_list = []
sum = 0
for i in range(N):
    L.append(sys.stdin.readline().rstrip())

dic = {
    'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0, 
}

for s in L:
    for i in range(len(s)):
        num = 10 ** (len(s)-i-1)
        dic[s[i]] += num
        
for value in dic.values():
    if(value>0):
        result_list.append(value)
result_list.sort(reverse=True)

for i in range(len(result_list)):
    sum += result_list[i]*(9-i)

print(sum)