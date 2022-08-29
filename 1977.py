
M = int(input())
N = int(input())
L = list()

for i in range(1,101):
    if(i*i >= M and i*i<= N):
        L.append(i*i)

if(len(L)==0):
    print(-1)
else:
    print(sum(L))
    print(min(L))
