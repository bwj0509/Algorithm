import sys
while(1):
    S = list(sys.stdin.readline().lower())
    if(S[0]=='#'):
        break
    alphabet = S[0]
    cnt = -1

    for i in S:
        if(i==alphabet):
            cnt += 1
    print(alphabet,cnt)