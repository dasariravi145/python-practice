x = int(input("Enter then number"))

for i in range(x,0,-1):
    for j in range(i,0,-1):
        print( chr(64+j), end=' ')
    print() 