import sys

N = int(sys.stdin.readline())

L = list(map(int, sys.stdin.readline().rstrip().split()))
upCnt = 0
upCnt_list = []
downCnt = 0
downCnt_list = []


for i in range(0, len(L)-1):
    if(L[i] <= L[i+1]):
        upCnt +=1
    else:
        upCnt_list.append(upCnt)
        upCnt=0


for i in range(0, len(L)-1):
    if(L[i] >= L[i+1]):
        downCnt +=1
    else:
        downCnt_list.append(downCnt)
        downCnt=0
        
        
upCnt_list.append(upCnt)
downCnt_list.append(downCnt)
print(max(max(downCnt_list),max(upCnt_list))+1)