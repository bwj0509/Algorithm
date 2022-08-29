import sys
from unittest import result

N = int(sys.stdin.readline())
ans = 0
alpha = []
L = []
dic = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
       'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

for _ in range(N):
    alphabet = sys.stdin.readline().rstrip()
    alpha.append(alphabet)

for alpa in alpha:
    for i in range(len(alpa)):
        num = 10 ** (len(alpa)-i-1)
        dic[alpa[i]] += num


for value in dic.values():
    if value > 0:
        L.append(value)

sorted_list = sorted(L, reverse=True)
for i in range(len(sorted_list)):
    ans += sorted_list[i] * (9 - i)

print(ans)
