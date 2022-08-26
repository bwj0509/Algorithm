import sys

n = int(sys.stdin.readline())
L = []
for i in range(n):
    name, day, month, year = map(str, sys.stdin.readline().split())
    L.append([name, day, month, year])

L.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(L[-1][0])
print(L[0][0])
