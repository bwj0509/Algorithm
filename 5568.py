import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
L = []
result_list = []
for _ in range(n):
    a = int(sys.stdin.readline())
    L.append(a)
    
if(k==2):
    for i in range(len(L)):
        for j in range(len(L)):
            if(i!=j):
                result_list.append(str(L[i])+str(L[j]))
elif(k==3):
        for i in range(len(L)):
            for j in range(len(L)):
                for k in range(len(L)):
                    if(i!=j and i!=k and j!=k):
                        result_list.append(str(L[i])+str(L[j])+str(L[k]))
elif(k==4):
        for i in range(len(L)):
            for j in range(len(L)):
                for k in range(len(L)):
                    for l in range(len(L)):
                        if(i!=j and i!=k and i!=l and j!=k and j!=l and k!=l):
                            result_list.append(str(L[i])+str(L[j])+str(L[k])+str(L[l]))


result_list = len(list(set(result_list)))
print(result_list)