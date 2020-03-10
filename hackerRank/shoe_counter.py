from collections import Counter

noOfShoes = int(input())
shoeList = Counter(input().split(" "))
noOfCostumer = int(input())
sum =0
orders = [input().split() for _ in range(noOfCostumer)] # key price

for size,price in orders:
    for sz,no in shoeList.items():
        if size == sz and no > 0:
            sum += int(price)
            shoeList[sz] = int(shoeList[sz]) -1  #itta sochna tha bas
            

print(sum)