n=int(input())
original=n
reverse=0
while n!=0:
    last=n%10
    reverse=reverse*10+last
    n=n//10

print(reverse)

if reverse==original:
    print("palindrome")
else:
    print("not palindrome")


#alter reverse number code program by storing initial n doing palindrome check