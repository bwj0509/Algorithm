import sys

N = int(sys.stdin.readline())
L = list(map(int,sys.stdin.readline().split()))
L.sort()

sum = 0
for i in range(N):
    sum += L[i]*(N-i)
    
print(sum)