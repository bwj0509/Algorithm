from re import U
import sys


import sys

S = list(sys.stdin.readline())

L = ['U', 'C', 'P', 'C', 'end']

for i in S:
    if(i == L[0]):
        L.pop(0)

if(L[0] == 'end'):
    print('I love UCPC')
else:
    print('I hate UCPC')
