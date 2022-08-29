import sys

participant = []
completion = []

participant = list(map(str, sys.stdin.readline().split()))
completion = list(map(str, sys.stdin.readline().split()))


result = set(participant) - set(completion)

for i in result:
    print(i)
    
