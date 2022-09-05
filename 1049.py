import sys

N, M = map(int, sys.stdin.readline().split())
paymoney = 0
price_6 = []
price_1 = []
for _ in range(M):
    A,B = map(int, sys.stdin.readline().split())
    price_6.append(A)
    price_1.append(B)

    
minPirce1 = min(price_1)
minPrice6 = min(price_6)
per1price = minPrice6/6

if(minPrice6<minPirce1*6):
    paymoney += minPrice6 * (N//6)
    if(minPrice6<minPirce1*(N%6)):
        paymoney += minPrice6
    else:
        paymoney += minPirce1*(N%6)
else:
    paymoney += minPirce1*N
print(paymoney)

        