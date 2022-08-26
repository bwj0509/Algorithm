import sys

n = int(sys.stdin.readline())

for i in range(n):
    L = list(map(int, sys.stdin.readline().split()))
    L.sort()
    del L[0]
    del L[-1]

    if(L[-1]-L[0] >= 4):
        print('KIN')
    else:
        print(sum(L))
