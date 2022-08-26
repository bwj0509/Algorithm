import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
if(K >= N):
    print(0)
else:
    L = list(map(int, sys.stdin.readline().rstrip().split()))
    L.sort()

    L_diff = []
    for i in range(1, len(L)):
        a = L[i]-L[i-1]
        L_diff.append(a)

    L_diff.sort()

    for i in range(K-1):
        L_diff.pop()

    print(sum(L_diff))
