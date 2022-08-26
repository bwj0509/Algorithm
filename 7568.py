import sys

N = int(sys.stdin.readline())

L = []

for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    L.append([A, B, 1])

for i in range(N):
    for j in range(N):
        if(L[i][0] < L[j][0] and L[i][1] < L[j][1]):
            L[i][2] += 1

for i in L:
    print(i[2], end=' ')
