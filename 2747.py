import sys

L = [0,1]
N = int(sys.stdin.readline())
fibo = 0

for i in range(2,N+1):
    fibo = L[i-2]+L[i-1]
    L.append(fibo)
    
print(max(L))