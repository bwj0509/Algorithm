import sys

N = int(sys.stdin.readline())
L = []
av_cnt = 0
finish_time = 0

for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    L.append([A, B])
    

L.sort(key=lambda x:(x[1],x[0]))
for i in range(len(L)):
    if(L[i][0]>=finish_time):
        av_cnt +=1
        finish_time = L[i][1]
print(av_cnt)