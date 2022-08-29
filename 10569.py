import sys
result = 0

for i in range(int(sys.stdin.readline())):
    A, B = map(int, sys.stdin.readline().split())
    result = 2-A+B
    print(result)
