import sys
dic ={
        '-':0,
        '\\':1,
        '(':2,
        '@':3,
        '?':4,
        ">":5,
        '&':6,
        '%':7,
        '/':-1
    }
while(1):
    L = list(map(str, sys.stdin.readline().rstrip()))
    if(len(L)and L[0]=='#'):
        break
    sum = 0

    for i in range(len(L)):
        sum += (8**(len(L)-i-1))*dic[L[i]]
        
    print(sum)