import sys

N, K, L = map(int, sys.stdin.readline().split())
VIP_L = []
team = 0

for i in range(N):
    A, B, C = map(int, sys.stdin.readline().split())
    if(A+B+C >= K and A >= L and B >= L and C >= L):
        VIP_L.append(A)
        VIP_L.append(B)
        VIP_L.append(C)
        team += 1
    else:
        continue

print(team)
for i in VIP_L:
    print(i, end=' ')
