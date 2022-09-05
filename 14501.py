import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

L = list(map(int, sys.stdin.readline().rstrip().split()))
L.sort()

left, right = 0, len(L)-1
cnt = 0

while(left<right):
    sum_num = L[left]+L[right]
    if(sum_num)<M:
        left += 1
    elif(sum_num>M):
        right -= 1
    else:
        cnt +=1
        left +=1
        right -=1
        
print(cnt)