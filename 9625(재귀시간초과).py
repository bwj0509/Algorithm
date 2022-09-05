import sys

def cntB(num):
    if(num ==0):
        return 0
    elif(num == 1):
        return 1
    else:
        return cntB(num-1) + cntB(num-2)
    
def cntA(num):
    if(num ==0):
        return 1
    elif(num == 1):
        return 0
    elif(num == 2):
        return 1
    else:
        return cntA(num-1) + cntA(num-2)

K = int(sys.stdin.readline())

print(cntA(K), cntB(K))