import sys

N, K = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

cost_list = []

for i in range(len(L)-1):
    cost_list.append(L[i+1]-L[i])

cost_list.sort()

for _ in range(K-1):
    cost_list.pop()

print(sum(cost_list))
