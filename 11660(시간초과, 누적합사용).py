import sys

N, M = map(int, sys.stdin.readline().split())
L = []

for i in range(N):
    tmp = list(map(str, sys.stdin.readline().rstrip().split()))

    for i in tmp:
        L.append(int(i))


for i in range(M):
    x1, x2, y1, y2 = map(int, sys.stdin.readline().split())

    start_point = N*(x1-1) + x2
    end_point = N*(y1-1) + y2
    sum = 0
    for i in range(start_point, end_point+1):
        sum += L[i-1]
    print(sum)
