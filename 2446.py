N = int(input())

for i in range(1, N+1):
    print(' '*(i-1), end='')
    print('*'*((2*N)-(2*i-1)))
    
for i in range(1, N):
    print(' '*(N-i-1), end='')
    print('*'*(i*2+1))