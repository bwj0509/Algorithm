import sys

result = 1
for i in range(1, int(sys.stdin.readline())+1):
    result *= i
    
print(result)