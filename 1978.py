import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
count = 0

for i in L:
    if(i==1):
        count -=1
    for j in range(2,i):
        if(i%j==0):
            count += 1
    
print(count)