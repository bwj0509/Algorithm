import sys

N = int(sys.stdin.readline())
dp = [0]*1001

dp[1] = 1  # 1은 상근이의 승리 2는 창영이의 승리
dp[3] = 1
dp[4] = 1

for i in range(5, N+1):
    if(dp[i-4] == 1 and dp[i-3] == 1 and dp[i-1] == 1):
        dp[i] = 0
    else:
        dp[i] = 1

if(dp[N] == 1):
    print('SK')
else:
    print('CY')
