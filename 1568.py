import sys


N = int(sys.stdin.readline())

cnt = 0
num = 1

while(N != 0):
    if(N > 0 and N-num >= 0):
        N = N-num
        cnt += 1
        num += 1
    else:
        num = 1

print(cnt)
