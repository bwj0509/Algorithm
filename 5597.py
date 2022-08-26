import sys

L = [0]*31
L[0] = 1

for i in range(28):
    n = int(sys.stdin.readline())
    L[n] = 1


for i in range(len(L)):
    if(L[i] == 0):
        print(i)
