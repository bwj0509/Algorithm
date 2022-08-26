import sys
import math

cnt = 1
while(1):
    A, B, C = map(int, sys.stdin.readline().split())

    if(A == 0 and B == 0 and C == 0):
        break

    if(C == -1):
        C = (A**2)+(B**2)
        C = math.sqrt(C)
        print('Triangle #%d' % cnt)
        print('c = %.3f' % C)
        print('')

    if(B == -1):
        if(A >= C):
            print('Triangle #%d' % cnt)
            print('Impossible.')
            print('')
        else:
            B = (C**2)-(A**2)
            B = math.sqrt(B)
            print('Triangle #%d' % cnt)
            print('b = %.3f' % B)
            print('')

    if(A == -1):
        if(B >= C):
            print('Triangle #%d' % cnt)
            print('Impossible.')
            print('')
        else:
            A = (C**2)-(B**2)
            A = math.sqrt(A)
            print('Triangle #%d' % cnt)
            print('a = %.3f' % A)
            print('')

    cnt += 1
