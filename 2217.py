import sys

N = int(sys.stdin.readline())
L = []
ans = []
for i in range(N):
    L.append(int(sys.stdin.readline()))
L.sort()
for j in L:
    ans.append(j*N)
    N -=1

print(max(ans))