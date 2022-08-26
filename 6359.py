import sys


n = int(sys.stdin.readline())

for i in range(n):
    A, B, C = map(int, sys.stdin.readline().split())
    L = [A, B, C]
    L.sort()
    if(L[2]**2 == L[0]**2 + L[1]**2):
        print('Scenario #%d:' % (i+1))
        print('yes')
        print('')
    else:
        print('Scenario #%d:' % (i+1))
        print('no')
        print('')
