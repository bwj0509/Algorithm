import sys

N = int(sys.stdin.readline().rstrip())

maker = []

if(N <= 10):
    if(N % 2 == 0):
        maker.append(int(N/2))
else:
    for i in range(1, N):
        L = list(map(int, str(i)))
        if(N == (sum(L)+i)):
            maker.append(i)

if(len(maker) == 0):
    print(0)
else:
    print(min(maker))
