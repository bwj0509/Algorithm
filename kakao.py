import sys

survey = list(map(str, sys.stdin.readline().split()))
choice = list(map(str, sys.stdin.readline().split()))

result = [0,0,0,0,0,0,0,0]
MBTI_result = [0,0,0,0]
for i in range(len(survey)):
    #RT,TR 유형
    if(survey[i]=='RT'):
        if(int(choice[i])>4):
            result[1] += int(choice[i])-4
        elif(int(choice[i])<4):
            result[0] += 3- int(choice[i]) +1
    if(survey[i]=='TR'):
        if(int(choice[i])>4):
            result[0] += int(choice[i])-4
        elif(int(choice[i])<4):
            result[1] += 3- int(choice[i]) +1
            
    if(survey[i]=='CF'):
        if(int(choice[i])>4):
            result[3] += int(choice[i])-4
        elif(int(choice[i])<4):
            result[2] += 3- int(choice[i]) +1
    if(survey[i]=='FC'):
        if(int(choice[i])>4):
            result[2] += int(choice[i])-4
        elif(int(choice[i])<4):
            result[3] += 3- int(choice[i]) +1
            
    if(survey[i]=='JM'):
        if(int(choice[i])>4):
            result[5] += int(choice[i])-4
        elif(int(choice[i])<4):
            result[4] += 3- int(choice[i]) +1
    if(survey[i]=='MJ'):
        if(int(choice[i])>4):
            result[4] += int(choice[i])-4
        elif(int(choice[i])<4):
            result[5] += 3- int(choice[i]) +1
            
    if(survey[i]=='AN'):
        if(int(choice[i])>4):
            result[7] += int(choice[i])-4
        elif(int(choice[i])<4):
            result[6] += 3- int(choice[i]) +1
    if(survey[i]=='NA'):
        if(int(choice[i])>4):
            result[6] += int(choice[i])-4
        elif(int(choice[i])<4):
            result[7] += 3- int(choice[i]) +1

if(result[0]>=result[1]):
    MBTI_result[0] = "R"
else:
    MBTI_result[0] = "T"
if(result[2]>=result[3]):
    MBTI_result[1] = "C"
else:
    MBTI_result[1] = "F"
if(result[4]>=result[5]):
    MBTI_result[2] = "J"
else:
    MBTI_result[2] = "M"
if(result[6]>=result[7]):
    MBTI_result[3] = "A"
else:
    MBTI_result[3] = "N"


for i in MBTI_result:
    print(i,end='')