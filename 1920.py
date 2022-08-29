import sys


def binary_search(array, target, start, end):
    while(start <= end):
        mid = (start+end) // 2
        if(array[mid] == target):
            return mid
        elif(array[mid] > target):
            end = mid - 1
        else:
            start = mid+1
    return None


N = int(sys.stdin.readline())
have_List = list(map(int, sys.stdin.readline().rstrip().split()))
have_List.sort()  # sort!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

M = int(sys.stdin.readline())
want_List = list(map(int, sys.stdin.readline().rstrip().split()))


for i in range(M):
    result = binary_search(have_List, want_List[i], 0, N-1)
    if(result == None):
        print(0)
    else:
        print(1)
