import sys
def binary_search(array, target, start, end):
    while(start<=end):
        mid = (start + end) // 2
        if(array[mid]==target):
            return mid
        elif(array[mid]>=target):
            end = mid -1
        else:
            start = mid +1
    return None

N = int(sys.stdin.readline())
have_list = list(map(int, sys.stdin.readline().split()))
have_list.sort()

M = int(sys.stdin.readline()) #찾아야 할 값으로 지정
want_list = list(map(int, sys.stdin.readline().split()))


for i in range(M):
    result = binary_search(have_list, want_list[i], 0, N-1)
    
    if(result == None):
        print('0', end=' ')
    else:
        print('1', end=' ')

