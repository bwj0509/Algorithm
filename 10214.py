Y_Score = K_Score = 0

for _ in range(int(input())):

    for i in range(9):
        A, B = map(int, input().split())
        Y_Score += A
        K_Score += B

    if(Y_Score>K_Score):
        print('Yonsei')
    elif(K_Score>Y_Score):
        print('Korea')
    else:
        print('Draw')