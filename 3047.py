import sys


number_L = list(map(int, sys.stdin.readline().split()))
number_L.sort()

L = list(sys.stdin.readline().rstrip())

for i in L:

    if(i == 'A'):
        print(number_L[0], end=' ')
    elif(i == 'B'):
        print(number_L[1], end=' ')
    else:
        print(number_L[2], end=' ')
