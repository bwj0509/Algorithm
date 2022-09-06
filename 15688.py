from re import I
import sys
L = []
for _ in range(int(sys.stdin.readline())):
    L.append(int(sys.stdin.readline()))

L.sort()

for i in L:
    print(i)