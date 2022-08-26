import sys


n = int(sys.stdin.readline())

while(1):
    su = int(sys.stdin.readline())
    if(su == 0):
        break

    if(su % n == 0):
        print('%d is a multiple of %d.' % (su, n))
    else:
        print('%d is NOT a multiple of %d.' % (su, n))
