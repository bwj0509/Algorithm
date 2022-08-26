import sys

N, C = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
L = []
for i in range(M):
    A, B, BOX = map(int, sys.stdin.readline().split())
    L.append([A, B, BOX])

L.sort(key=lambda x: (x[1], x[0]))
print(L)
complete_box = 0
