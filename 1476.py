
import sys
E, S, M, year = 1, 1,1, 1

E_cal, S_cal, M_cal = map(int, sys.stdin.readline().split())

while(1):
    if(E_cal == E and S_cal == S and M_cal == M):
        break
    E+=1; S+=1; M+=1; year+=1
    
    if(E>=16):
        E -=15
    if(S>=29):
        S -= 28
    if(M>=20):
        M-=19

print(year)