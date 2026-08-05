rows=int(input())
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

rows1 = int(input())

for i in range(1, rows1 + 1):
    for j in range(rows1, i - 1, -1):
        print(j, end="")
    print()