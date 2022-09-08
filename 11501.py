import sys
for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    L = list(map(int, sys.stdin.readline().split()))

    L.reverse()
    value = 0
    max = 0

    for i in range(len(L)):
        if(L[i]>max):
            max = L[i]
        else:
            value += max-L[i]
    print(value)