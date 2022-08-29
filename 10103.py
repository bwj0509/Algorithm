A_Score = 100
B_Score = 100

for i in range(int(input())):
    A, B = map(int, input().split())
    if(A>B):
        B_Score -= A
    elif(B>A):
        A_Score -= B
        
print(A_Score)
print(B_Score)