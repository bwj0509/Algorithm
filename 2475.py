import sys

L = list(map(int, sys.stdin.readline().split()))
sum = 0
for i in L:
    sum += i*i
print(int(sum%10))