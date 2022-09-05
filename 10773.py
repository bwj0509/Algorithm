import sys

N = int(sys.stdin.readline())
L = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if(num!=0):
        L.append(num)

    else:
        L.pop()

print(sum(L))