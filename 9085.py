import sys

for i in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    L = list(map(int, sys.stdin.readline().split()))
    count = 0
    for i in L:
        count += i
    print(count)