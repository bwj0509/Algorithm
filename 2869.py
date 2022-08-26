import sys
import math


A, B, V = map(int, sys.stdin.readline().split())

day = 1
day += math.ceil(((V-A)/(A-B)))

print(day)
