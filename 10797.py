import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

N = int(N%10)
count = 0
for i in L:
    if(i==N):
        count += 1
        
print(count)