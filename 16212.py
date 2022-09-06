import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

L.sort()

for i in L:
    print(i)