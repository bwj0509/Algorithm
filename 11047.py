
import sys
L = []
N, K = map(int, sys.stdin.readline().split())

for i in range(N):
    coin = int(sys.stdin.readline())
    L.append(coin)

L.sort()
L.reverse()
cnt = 0

for i in range(len(L)):
    if(K != 0):
        cnt += int(K/L[i])
        K = K % L[i]
print(cnt)
