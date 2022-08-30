import sys
import time

N = int(sys.stdin.readline())
have_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
want_list = list(map(int, sys.stdin.readline().split()))
result_list = [0]*M

start = time.time()

for i in range(len(want_list)):
    for j in range(len(have_list)):
        if(want_list[i]==have_list[j]):
            result_list[i]=1
            
for i in result_list:
    print(i, end=' ')

print(time.time()-start)