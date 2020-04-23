    # Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = input().split(" ")
B = input().split(" ")

A = [int(i) for i in A] #converting in list of int from str
B = [int(i) for i in B]

cart = sorted( list( product(A, B ) ) )


for val in cart:
    print(val)