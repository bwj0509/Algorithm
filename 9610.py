Q1_cnt = 0
Q2_cnt = 0
Q3_cnt = 0
Q4_cnt = 0
AXIS_cnt = 0

for i in range(int(input())):
    A, B  = map(int, input().split())
    if(A>0 and B>0):
        Q1_cnt += 1
    elif(A>0 and B<0):
        Q4_cnt += 1
    elif(A<0 and B>0):
        Q2_cnt += 1
    elif(A<0 and B<0):
        Q3_cnt += 1
    else:
        AXIS_cnt +=1
        
print('Q1: %d'%Q1_cnt)
print('Q2: %d'%Q2_cnt)
print('Q3: %d'%Q3_cnt)
print('Q4: %d'%Q4_cnt)
print('AXIS: %d'%AXIS_cnt)