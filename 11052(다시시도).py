import sys


N = int(sys.stdin.readline())
N_remain = N
price = 0
L = list(map(int, sys.stdin.readline().split()))
L_per = []
for i in range(len(L)):
    a = L[i]/(i+1)
    L_per.append(a)


if(N_remain % L_per.index(max(L_per)+1) == 0):
    price = int(N_remain / L_per.index(max(L_per)))
    print(price)
