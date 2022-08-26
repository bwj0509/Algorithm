import sys

N = int(sys.stdin.readline())

result = 0
cnt = 1

while(1):
    if('666' in str(cnt)):
        result += 1
    if(N == result):
        print(cnt)
        break
    cnt += 1
