cute_cnt = 0
not_cute_cnt = 0

for i in range(int(input())):
    a = int(input())
    if(a==1):
        cute_cnt +=1
    else:
        not_cute_cnt +=1

if(cute_cnt>not_cute_cnt):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')