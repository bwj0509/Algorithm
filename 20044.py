import sys

n = int(sys.stdin.readline())

L = list(map(int, sys.stdin.readline().rstrip().split()))
L.sort()
L_power = []
for i in range(n):
    power = L[i]+L[-(i+1)]
    L_power.append(power)
print(min(L_power))
