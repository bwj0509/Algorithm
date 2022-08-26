import sys

N = int(sys.stdin.readline())
L = []

for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    L.append([A, B])

L.sort(key=lambda x: (x[0], x[1]))

for i in L:
    print(i[0], i[1])
