N = list(input())
height = 10

for i in range(1, len(N)):
    if(N[i-1] == N[i]):
        height += 5
    else:
        height += 10

print(height)
