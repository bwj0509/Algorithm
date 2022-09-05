import sys


fibo_list = [0,1,1]

for i in range(3,50):
    fibo_list.append(fibo_list[i-2]+fibo_list[i-1])

cnt_0_list = [1] +fibo_list
cnt_1_list = [] + fibo_list

for i in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    print(cnt_0_list[N], cnt_1_list[N])