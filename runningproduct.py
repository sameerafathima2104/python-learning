def runningProduct(nums):
    product=[]
    p=1
    for i in nums:
        p=p*i
        product.append(p)

    return product
nums=list(map(int,input("ENTER NUMBERS:").split()))
print(runningProduct(nums))