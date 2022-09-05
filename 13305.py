import sys

N = int(sys.stdin.readline())

distance_list = list(map(int, sys.stdin.readline().split()))
oilprice_list = list(map(int, sys.stdin.readline().split()))

min_price = 1000000001
pricesum = 0

for i in range(len(distance_list)):
    if(oilprice_list[i]<min_price):
        min_price = oilprice_list[i]
        pricesum = pricesum + (min_price*distance_list[i])
    else:
        pricesum = pricesum+ (min_price*distance_list[i])

print(pricesum)
