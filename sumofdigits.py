n=int(input())
original=n
check=n
total=0
count=0
while n!=0:
    n=n//10
    count=count+1

while check!=0:
    last=check%10
    total=total+(last**count)
    check=check//10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


