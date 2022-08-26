import sys

N = 1000 - int(sys.stdin.readline())
coin = 0

coin += int(N/500)
N %= 500

coin += int(N/100)
N %= 100

coin += int(N/50)
N %= 50

coin += int(N/10)
N %= 10

coin += int(N/5)
N %= 5

coin += N

print(coin)
