from collections import Counter

noOfShoes = int(input())
shoeList = Counter(input().split(" "))
noOfCostumer = int(input())

orders = [input().split() for _ in range(noOfCostumer)]

print(orders)
print(shoeList)