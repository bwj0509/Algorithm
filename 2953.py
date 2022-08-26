import sys

L = []

for i in range(5):
    A, B, C, D = map(int, sys.stdin.readline().split())
    L.append(A+B+C+D)
print(L.index(max(L))+1, max(L))
