import sys

for i in range(int(sys.stdin.readline())):
    A, B = map(int, sys.stdin.readline().split())
    
    print('You get %d piece(s) and your dad gets %d piece(s).'%(int(A/B),int(A%B)))