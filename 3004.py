import sys

N = int(sys.stdin.readline())


L = list(0 for i in range(100))
L[0] = 2
for i in range(1, 100):
    L[i] = int((i+1)/2)+1 + L[i-1]

print(L[N-1])
