import math

t = int(input())

for i in range(t):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(math.lcm(a, b))
