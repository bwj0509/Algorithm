import sys

N = int(sys.stdin.readline())
L = []
for _ in range(N):
    L.append(int(sys.stdin.readline()))

L.sort(reverse=True)

cnt=1
sum = 0

for i in range(len(L)):
    if(cnt==3):
        cnt = 1
    else:
        sum+= L[i]
        cnt+=1
        
print(sum)




