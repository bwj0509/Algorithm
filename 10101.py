import sys


A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

if((A+B+C) != 180):
    print('Error')
else:
    if(A == 60 and B == 60 and C == 60):
        print('Equilateral')
    elif(A == B or A == C or B == C):
        print('Isosceles')
    else:
        print('Scalene')
