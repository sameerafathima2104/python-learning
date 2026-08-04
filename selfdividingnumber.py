num=input()
selfdiv=True
for digit in num:
    if int(digit)==0 or int(num)%int(digit)!=0:
        selfdiv=False
        break
if selfdiv:
    print("Self div number")
else:
    print("no")