
for i in range(int(input())):
    P = int(input())
    L = list()

    for i in range(P):
        A, B = input().split()
        L.append([A,B])

    L.sort(key=lambda x:int(x[0]))
    
    print(L[len(L)-1][1])