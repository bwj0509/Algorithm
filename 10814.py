import sys

N = int(sys.stdin.readline())
L = []

for i in range(N):
    A, B = sys.stdin.readline().split()
    L.append([int(A), B])

L.sort(key=lambda x: (x[0]))

for i in L:
    print(i[0], i[1])
