ipt1 = int(input())
A = input().split()
ipt2 = int(input())
B = input().split()

A = set(map(int,A))
B = set(map(int,B))

sym = (A.difference(B)).union(B.difference(A))

symList = sorted(list(sym))
print(*symList,sep = "\n")
