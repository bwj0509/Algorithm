for _ in range(int(input())):
    T = int(input())
    sum = 0
    sub_cnt = 0


    for i in range(T):
        A, B = map(float, input().split())
        sum += A*B
        sub_cnt += A
    avg = sum/sub_cnt
    print(int(sub_cnt),round(avg,1))