import sys

L = []
ans = 0
for i in range(9):
    N = int(sys.stdin.readline())
    L.append(N)

for i in L:
    ans += i
ans -= 100

delete = []

for i in L:
    for j in L:
        if(i != j):
            if(i+j == ans):
                delete.append(i)
                delete.append(j)

result = set(L) - set(delete)

for i in result:
    print(i, end=' ')
