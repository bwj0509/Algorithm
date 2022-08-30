import sys

N = int(sys.stdin.readline())
min_sum= 0
A_list = list(map(int, sys.stdin.readline().split()))
B_list = list(map(int, sys.stdin.readline().split()))

A_list.sort()
B_list.sort(reverse=True)

for i in range(N):
    min_sum += A_list[i]*B_list[i]
print(min_sum)