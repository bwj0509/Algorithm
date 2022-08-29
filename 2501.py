import sys

N, K = map(int, sys.stdin.readline().split())

L = []
for i in range(1,N+1):
    if(N%i==0):
        L.append(i)
if(len(L)<K):
    print(0)
else:
    print(L[K-1])