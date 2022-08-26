import sys


T = int(sys.stdin.readline())

for i in range(T):
    cnt = 0
    N, D = map(int, sys.stdin.readline().split())
    for i in range(N):
        V, F, C = map(int, sys.stdin.readline().split())
        if(V*F/C >= D):
            cnt += 1
    print(cnt)
