import sys

N = int(sys.stdin.readline())
result_list = []
for i in range(N):
    result = 0
    A, B, C, D = map(int, sys.stdin.readline().split())
    
    L=[A, B, C, D]
    
    
    if(A==B and A==C and A==D):
        result = 50000+(A*5000)
    elif(A==B and A==C):
        result = 10000+(A*1000)
    elif(B==C and C==D):
        result = 10000+(B*1000)
    elif(A==C and C==D):
        result = 10000+(A*1000)
    elif(A==B and B==D):
        result = 10000+(A*1000)
    elif(A==B and C==D):
        result = 2000+(500*A)+(500*C)
    elif(A==C and B==D):
        result = 2000+(500*A)+(500*B)
    elif(A==D and B==C):
        result = 2000+(500*A)+(500*B)
    elif(A==B):
        result = 1000+(A*100)
    elif(A==C):
        result = 1000+(A*100)    
    elif(A==D):
        result = 1000+(A*100)    
    elif(B==C):
        result = 1000+(B*100)    
    elif(B==D):
        result = 1000+(B*100)    
    elif(C==D):
        result = 1000+(C*100)    
    else:
        result = 100*(max(L))
        
    
    result_list.append(result)

print(max(result_list))
    
    