rows=int(input())
for i in range(1,rows+1):
    for j in range(i):
        print("*",end="")
    print()

rows1=int(input())
for i in range(rows1,0,-1):
    for j in range (i):
         print("*",end="")
    print()