import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
re = A*B*C
result = list(map(int,str(re)))

for i in range(10):
    print(result.count(i))

