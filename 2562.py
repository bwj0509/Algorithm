import sys

L = []
max_index = 0

for i in range(9):
    N = int(sys.stdin.readline())
    L.append(N)
    if(max(L)<=N):
        max_index = i+1
    
print(max(L))
print(max_index)