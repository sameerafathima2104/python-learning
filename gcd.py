a=int(input())
b=int(input())
ans=1
small=min(a,b)
for i in range(1,small+1):
    if a%i==0 and b%i==0:
        ans=i
print(ans)