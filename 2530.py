A, B, C = map(int, input().split())
T = int(input())

if(C+T>59):
    B += int((C+T)/60)
    C = int((C+T)%60)
else:
    C = C+T

if(B>59):
    A += int(B/60)
    B = int(B%60)

if(A>23):
    A = A % 24

print(A, B, C)