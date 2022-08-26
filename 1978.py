import sys
N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
sosu_cnt = 0
for i in L:
    cnt = 0
    for j in range(1, i+1):
        if(i % j == 0):
            cnt += 1
    if(cnt == 2):
        sosu_cnt += 1

print(sosu_cnt)
