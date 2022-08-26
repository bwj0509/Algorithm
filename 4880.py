import sys

while(1):
    A, B, C = map(int, sys.stdin.readline().split())
    if(A == 0 and B == 0 and C == 0):
        break
    if(C-B == B-A):
        print('AP %d' % (C+(C-B)))
    else:
        print('GP %d' % (C*int(C/B)))
