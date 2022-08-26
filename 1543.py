from gettext import find
import sys

document = sys.stdin.readline().rstrip()
find_S = sys.stdin.readline().rstrip()


if(find_S in document):
    document = document.replace(find_S, '#')

result = document.count('#')
print(result)
