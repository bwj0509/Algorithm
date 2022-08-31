import sys

N = list(map(int, sys.stdin.readline().rstrip()))

jarisuhab = 0
for i in N:
    jarisuhab += i

if(jarisuhab%3==0 and N.count(0)>=1):
    N.sort(reverse=True)
    for i in N:
        print(i, end='')
else:
    print(-1)
    


