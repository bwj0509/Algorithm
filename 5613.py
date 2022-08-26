import sys


result = int(sys.stdin.readline())

while(1):
    operation = sys.stdin.readline().rstrip()
    if(operation == '='):
        break
    n = int(sys.stdin.readline())
    if(operation == '+'):
        result += n
    elif(operation == '-'):
        result -= n
    elif(operation == '*'):
        result *= n
    else:
        result = int(result/n)

print(result)
