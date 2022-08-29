import sys

N = int(sys.stdin.readline())
av = 1

for i in range(N):
    A = int(sys.stdin.readline())
    av += A -1
        
print(av)