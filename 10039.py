L = list()
sum = 0
for i in range(5):
    a = int(input())
    L.append(a)

for i in range(len(L)):
    if(L[i] < 40):
        L[i] = 40
    sum += L[i]


print(int(sum / len(L)))
