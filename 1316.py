import sys

N = int(sys.stdin.readline())
cnt = 0
for _ in range(N):
    S = list(sys.stdin.readline().rstrip())
    new_S = [S[0]]
    for i in range(1,len(S)):
        if(S[i]!=S[i-1]):
            new_S.append(S[i])
    
    result1 = dict.fromkeys(new_S)
    result2 = list(result1)
    
    if(new_S == result2):
        cnt += 1
        
print(cnt)

