import sys

n = int(sys. stdin.readline())

L = [0]*50
L[0] = 1
L[1] = 1
L[2] = 2
L[3] = 5

if(n>3):
    for i in range(4,n+1):
            for j in range(i):
                L[i] += L[j]*L[i-j-1]

print(L[n])