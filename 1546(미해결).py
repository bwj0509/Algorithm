import sys

N = int(sys.stdin.readline())

L = list(map(int, sys.stdin.readline().split()))
maxNum = max(L)
sum = 0

for i in L:
    sum += (i/maxNum*100)
    
print(sum/N)