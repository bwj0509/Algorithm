import sys

N, K = map(int, sys.stdin.readline().split())
L = []
for i in range(1, N+1):
    L.append(i)
yosefus = []
before_index = 0
while(len(L) != 0):
    if(len(L) >= K+before_index):
        yosefus.append(L[-1+K])
        del L[-1+K]
        before_index = -1+K
    else:
        i = int(K % len(L))
        yosefus.append(L[i])
        del L[-1+i]
        before_index = -1+i

print(yosefus)
