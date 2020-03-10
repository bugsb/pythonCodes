    # Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = input().split(" ")
B = input().split(" ")

A = [int(i) for i in A]
B = [int(i) for i in B]

cart = list(product(A,B))


print(*sorted(cart))