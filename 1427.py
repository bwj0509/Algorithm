import re
import sys


N = list(map(int, str(sys.stdin.readline().rstrip())))

N.sort(reverse=1)

for i in N:
    print(i, end='')
