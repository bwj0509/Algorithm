import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    L = list(map(int, sys.stdin.readline().split()))
    avg = round(sum(L)/n)
    L.sort()
    result = (L[-1]-L[0])*2
    print(result)
