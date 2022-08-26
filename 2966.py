import sys

sanggun = ['A', 'B', 'C', ]*34
changyoung = ['B', 'A', 'B', 'C']*25
hyunjin = ['C', 'C', 'A', 'A', 'B', 'B']*18

sanggun_score = 0
changyoung_score = 0
hyunjin_score = 0

N = int(sys.stdin.readline())
L = list(map(str, sys.stdin.readline().rstrip()))

for i in range(N):
    if(sanggun[i] == L[i]):
        sanggun_score += 1
    if(changyoung[i] == L[i]):
        changyoung_score += 1
    if(hyunjin[i] == L[i]):
        hyunjin_score += 1

print(max(sanggun_score, changyoung_score, hyunjin_score))

if(sanggun_score >= changyoung_score and sanggun_score >= hyunjin_score):
    print('Adrian')
if(changyoung_score >= sanggun_score and changyoung_score >= hyunjin_score):
    print('Bruno')
if(hyunjin_score >= sanggun_score and hyunjin_score >= changyoung_score):
    print('Goran')
