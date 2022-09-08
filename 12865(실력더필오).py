import sys

N, K = map(int, sys.stdin.readline().split())
L =[]
for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    WV = V/W
    L.append([W, V, WV])
    
L.sort(key=lambda x:x[2], reverse=True)
print(L)
    


