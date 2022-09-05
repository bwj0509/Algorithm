import sys

L = []

N, M = map(int, sys.stdin.readline().split())

for _ in range(N):
    L += list(map(int, sys.stdin.readline().rstrip().split()))

for _ in range(M):  
    sum = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    start = (x1-1)*N+(y1-1)
    end = (x2-1)*N+(y2-1)

    for i in range(start, end+1):
        sum += L[i]
    print(sum)
