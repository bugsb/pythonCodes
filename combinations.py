from itertools import combinations
l = []

string,key = input().split()
for i in range(1,int(key)+1):
    elements = (list(combinations(sorted(string),i)))

    for j in elements:
        print(*j,sep="")