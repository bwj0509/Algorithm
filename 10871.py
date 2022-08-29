import sys


N, X = map(int, sys.stdin.readline().split())

L = list(map(int,(sys.stdin.readline().split())))
result = []

for i in L:
    if(i<X):
        print(i, end=' ')

