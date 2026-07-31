n=int(input())
isprime=True
if n<=1:
    isprime=False
else:
    for i in range(2,n):
        if n%i==0:
            isprime=False
            break

if isprime:
    print("Prime")
else:
    print("notprime")