T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    sum = A+B
    print('Case #%d: %d + %d = %d'%((i+1),A,B,sum))