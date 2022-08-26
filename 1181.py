import sys

N = int(sys.stdin.readline().rstrip())
L = []


for i in range(N):
    L.append(input())

L = list(set(L))
L.sort()
L.sort(key=lambda x: (len(x)))

for i in L:
    print(i)


n = int(input())
a = []
for i in range(0, n):
    a.append(input())
a = list(set(a))
a.sort()
a.sort(key=len)

for i in a:
    print(i)
