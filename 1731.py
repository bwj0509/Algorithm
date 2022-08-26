import sys

N = int(sys.stdin.readline())
L = []

for i in range(N):
    L.append(int(sys.stdin.readline()))

if(L[1]*2 == L[0]+L[2]):
    dif = L[2]-L[1]
    result = L[N-1]+dif
else:
    dif = int(L[2]/L[1])
    result = L[N-1]*dif

print(result)
