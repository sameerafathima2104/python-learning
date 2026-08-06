n=int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+i),end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()
for i in range(n):
    for j in range(n - i):
        print(chr(65 + j), end="")
    print()