from itertools import permutations
inp = input().split()

per = list(permutations(sorted(inp[0]),int(inp[1])))

str = ""
for val in per:
    str = "".join(val)
    print(str)