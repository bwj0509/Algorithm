for i in range(int(input())):

    S = list(input())
    cnt = 0
    score = 0

    for i in S:
        if(i=='O'):
            cnt +=1
            score += cnt
        else:
            cnt = 0
    
    print(score)
    