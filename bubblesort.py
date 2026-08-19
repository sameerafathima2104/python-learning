arr=[20,89,76,54,31,46]
for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)