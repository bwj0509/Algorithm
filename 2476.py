L = list()

for i in range(int(input())):
    A, B, C = map(int, input().split())
    if(A==B==C):
        L.append(10000+A*1000)
    elif(A==B):
        L.append(1000+A*100)
    elif(A==C):
        L.append(1000+A*100)
    elif(B==C):
        L.append(1000+B*100)
    else:
        L.append(max(A,B,C)*100)

print(max(L))