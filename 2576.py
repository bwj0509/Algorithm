import sys
L=[]
L_hol =[]
sum = 0
for i in range(7):
    L.append(int(sys.stdin.readline()))

for i in L:
    if(i%2==1):
        L_hol.append(i)
        sum += i

if(sum==0):
    print(-1)
else:
    print(sum)
    print(min(L_hol))