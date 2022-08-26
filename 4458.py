import sys

N = int(sys.stdin.readline())

for i in range(N):
    L = list(map(str, sys.stdin.readline().rstrip()))
    L[0] = L[0].upper()
    for i in L:
        print(i, end='')
    print('')
