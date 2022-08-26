L = [0]*11000
L[0] = 1

for i in range(1, 10001):
    new_num = i + sum(map(int, str(i)))
    L[new_num] = 1

for i in range(1, 10001):
    if(L[i] == 0):
        print(i)
