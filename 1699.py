import math
import sys
print(math.sqrt(98989))

N = int(sys.stdin.readline())
cnt = 0

for i in range(int(math.sqrt(N)), 0, -1):
    cnt += int(N / i**2)
    N = N % i**2
print(cnt)


#

N = int(sys.stdin.readline())

# 각각의 수를 1^2 으로 표현할때가 가장 큰 횟수이기 때문에 인덱스와 동일하게 x로 초기화
dp = [x for x in range(N+1)]


for i in range(1, N + 1):
    for j in range(1, int(math.sqrt(i) + 1)):
        if dp[i] > (dp[i - j * j] + 1):
            dp[i] = dp[i - j * j] + 1

print(dp[N])
