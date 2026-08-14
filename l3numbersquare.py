start=int(input())
end=int(input())
result=[]
if start>end:
    print("invalid range")
elif start==end:
    print("Range is equal")
else:
    for i in range (start,end+1):
        result.append((i,i*i))
    print(result)