import sys
import copy

N = int(sys.stdin.readline())

L_1 = list(map(int, sys.stdin.readline().rstrip()))
L_2 = copy.deepcopy(L_1)
L_result = list(map(int, sys.stdin.readline().rstrip()))

L_1_cnt = 0
L_2_cnt = 0
L1_possible = 0
L2_possible = 0


for i in range(N):  # 첫수를 변경하는 경우
    if(i == 0):
        L_1[i] = 1 - L_1[i]
        L_1[i+1] = 1 - L_1[i+1]
        L_1_cnt += 1
    elif(i >= 1 and i < N-1):
        if(L_result[i-1] != L_1[i-1]):
            L_1[i-1] = 1 - L_1[i-1]
            L_1[i] = 1 - L_1[i]
            L_1[i+1] = 1 - L_1[i+1]
            L_1_cnt += 1
    else:
        if(L_result[i-1] != L_1[i-1]):
            L_1[i-1] = 1 - L_1[i-1]
            L_1[i] = 1 - L_1[i]
            L_1_cnt += 1
if(L_result == L_1):
    L1_possible = 1


for i in range(N):  # 첫수를 변경하지 않는 경우
    if(i == 0):
        x = 1
    elif(i >= 1 and i < N-1):
        if(L_result[i-1] != L_2[i-1]):
            L_2[i-1] = 1 - L_2[i-1]
            L_2[i] = 1 - L_2[i]
            L_2[i+1] = 1 - L_2[i+1]
            L_2_cnt += 1
    else:
        if(L_result[i-1] != L_2[i-1]):
            L_2[i-1] = 1 - L_2[i-1]
            L_2[i] = 1 - L_2[i]
            L_2_cnt += 1

if(L_result == L_2):
    L2_possible = 1


if(L1_possible == 1 and L2_possible == 1):
    if(L1_possible <= L2_possible):
        print(L_1_cnt)
    else:
        print(L_2_cnt)
elif(L1_possible == 1):
    print(L_1_cnt)
elif(L2_possible == 1):
    print(L_2_cnt)
else:
    print('-1')
