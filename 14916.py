import sys

n = int(sys.stdin.readline())
cnt = 0

if(n==1 or n==3):
    print(-1)
elif(n%5==1 or n%5==3):
    cnt += (n//5)-1
    cnt += ((n%5)+5)//2
    print(cnt)
else:
    cnt += n//5
    cnt += (n%5)//2
    print(cnt)