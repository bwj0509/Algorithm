import sys

N = int(sys.stdin.readline())
L = [0]*10001

for i in range(N):
    L[int(sys.stdin.readline())] +=1

for i in range(1, 10001):
    if(L[i] !=0):
        for _ in range(L[i]):
            print(i)