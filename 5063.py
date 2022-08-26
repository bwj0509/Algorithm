T = int(input())

for i in range(T):
    A, B, C = map(int, input().split())
    if(B-C > A):
        print('advertise')
    elif(B-C == A):
        print('does not matter')
    else:
        print('do not advertise')
