import sys

N = int(sys.stdin.readline())

L = list(map(int, sys.stdin.readline().split()))

L_check = [0]*len(L)

for i in range(len(L)-1):
    if(L[i+1]-L[i]>0):
        L_check[i+1] = 1
print(L_check.count(1)+1)