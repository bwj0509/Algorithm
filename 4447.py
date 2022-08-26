import sys

n = int(sys.stdin.readline())

for i in range(n):

    cnt_g = 0
    cnt_b = 0
    S = sys.stdin.readline().rstrip()
    L = list(map(str, S.rstrip()))

    for i in L:
        if(i == 'g' or i == 'G'):
            cnt_g += 1
        elif(i == 'b' or i == 'B'):
            cnt_b += 1

    if(cnt_g > cnt_b):
        print('%s is GOOD' % (S))
    elif(cnt_b > cnt_g):
        print('%s is A BADDY' % (S))
    else:
        print('%s is NEUTRAL' % (S))
