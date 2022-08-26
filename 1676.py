from math import factorial
import sys

N = int(sys.stdin.readline())
factorial_N = 1
for i in range(2, N+1):
    factorial_N *= i
active = True
cnt = 0

factorial_N_list = list(map(int, str(factorial_N)))

while(active):
    if(factorial_N_list.pop() == 0):
        cnt += 1
    else:
        break
print(cnt)
