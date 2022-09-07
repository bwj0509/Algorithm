import sys

n = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    L[i] = max(L[i], L[i-1]+L[i])

print(max(L))