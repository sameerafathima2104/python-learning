def runningSum(nums):
    sum=[]
    s=0
    for i in nums:
        s=s+i
        sum.append(s)

    return sum
nums=list(map(int,input("ENTER NUMBERS:").split()))
print(runningSum(nums))