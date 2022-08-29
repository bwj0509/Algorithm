T = int(input())
cnt = 0

for i in range(T):
    A, B = map(int, input().split())
    cnt+=int(B%A)

print(cnt)   