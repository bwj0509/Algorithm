
for i in range(int(input())):
    L = list()
    N = int(input())
    for i in range(N):
        A, B = map(str, input().split())
        L.append([A,B])
        
    L.sort(key=lambda x:(int(x[1])))
    print(L[-1][0])