A = 300
B = 60
C = 10

A_cnt = 0
B_cnt = 0
C_cnt = 0

T = int(input())

if(int(T/A) > 0):
    A_cnt = int(T/A)
    T = int(T%A)
if(int(T/B) > 0):
    B_cnt = int(T/B)
    T = int(T%B)
if(int(T/C) > 0):
    C_cnt = int(T/C)
    T = int(T%C)

if(T==0):
    print(A_cnt, B_cnt, C_cnt)
else:
    print(-1)

