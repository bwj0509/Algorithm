n = int(input())
L = [0,1,1]
for i in range(3,n+1):
    L.append(L[i-2]+L[i-1])
    
print(max(L))