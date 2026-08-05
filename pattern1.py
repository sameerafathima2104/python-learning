rows = int(input())

# i represents the number to be printed in each row
# range(1, rows + 1) means 1, 2, 3, ..., rows
for i in range(1, rows + 1):

    # Print i exactly i times
    # If i = 3, range(3) runs 3 times: 0, 1, 2
    for j in range(i):
        print(i, end="")

    # Move to the next line after finishing one row
    print()

rows1=int(input())
for i in range (rows1,0,-1):
    for j in range (i):
        print(i,end="")
    print()