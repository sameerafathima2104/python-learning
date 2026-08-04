n = int(input())

if n>0:
    for i in range(n,0,-1):
        print(i, end=" ")
elif n<0:
    for i in range(n + 1, 0):
        print(i, end=" ")

else:
    print("0")