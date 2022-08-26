import sys

T = int(sys.stdin.readline())

for i in range(T):
    cnt = 0
    n, m = map(int, sys.stdin.readline().split())

    for a in range(1, n):
        for b in range(1, n):
            if(b > a):
                cal_num = (a**2+b**2+m)/(a*b)
                if(int(cal_num) == cal_num):
                    cnt += 1

    print(cnt)
