N = int(input())

for i in range(1,N+1):
    print('*'*(i), end='')
    print(' '*(N-i),end='')
    print(' '*(N-i),end='')
    print('*'*(i))
    
for i in range(2,N+1):
    print('*'*(N-i+1), end='')
    print(' '*(i-1),end='')
    print(' '*(i-1),end='')
    print('*'*(N-i+1))