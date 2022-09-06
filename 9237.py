import sys

n = int(sys.stdin.readline())

day =1
L = list(map(int, sys.stdin.readline().split()))
L.sort(reverse=True)
for i in range(len(L)):
    L[i] += day
    day +=1
print(max(L)+1)