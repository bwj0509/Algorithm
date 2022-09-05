import sys

N = int(sys.stdin.readline())
L = []

for _ in range(N):
    L.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(1, len(L)):
    L[i][0]= min(L[i-1][1], L[i-1][2])+L[i][0]
    L[i][1]= min(L[i-1][0], L[i-1][2])+L[i][1]
    L[i][2]= min(L[i-1][0], L[i-1][1])+L[i][2]
print(min(L[N-1]))