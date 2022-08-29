import sys

T = int(sys.stdin.readline())

for i in range(T):
    if(i%2==1):
        print(' ', end='')
        print('* '*T)
    else:
        print('* '*T)
    