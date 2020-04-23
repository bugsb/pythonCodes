ipt = input().split(" ")

m = int(ipt[0])
n = int(ipt[1])

ml = [input() for _ in range( m ) ]
nl = [input() for _ in range( n ) ]

for i in range(len( nl ) ):
    if nl[i] not in ml:
        print(-1)
    else:
        for j in range(len( ml ) ):
            if nl[i] == ml[j]:
                print(j+1,end=" ")
            
        
        print()
        
