A, B = map(int, input().split())


if(B >= 45):
    B = B-45
elif(B <= 45):
    if(A == 0):
        A = 23
    else:
        A = A-1
    B = B+15


print(A, B)
