a=int(input())
b=int(input())
c=int(input())
sum=a+b+c;
if sum>180:
    print("Invalid triangle")
elif a==90 or b==90 or c==90:
    print("Right")
elif a<180 or b<180 or c<180:
    print("Obtuse")