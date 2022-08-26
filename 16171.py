import sys
import re

S = sys.stdin.readline()
K = sys.stdin.readline()

new_S = re.sub('[0-9]+', '', S)

if(K in new_S):
    print('1')
else:
    print('0')
