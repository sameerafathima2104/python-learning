words=input().split()
count=0
result=[]
for word in words:
    rev=word[::-1]
    if rev!=word and rev in words:
        count=count+1

print(count//2)