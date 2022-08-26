
import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

L = []
for i in range(M, N+1):
    for j in range(2, i+1):
        if j == i:
            L.append(i)
        if i % j == 0:
            break


if(len(L) == 0):
    print(-1)
else:
    print(sum(L))
    print(min(L))
