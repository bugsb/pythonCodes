sizeOfArray = int(input())

array = list(map(int,input().split()))
print(*array[::-1])