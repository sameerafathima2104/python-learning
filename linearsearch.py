x=[1,2,3,4,5]
a=7
for i in range(0,len(x)):
    if x[i]==a:
        print(i)
        break

#without index
for i in x:
    if i==a:
        print("yes")
else:
    print("no")