#count inside digit

n = input()
count = 0            #do not use in range instead use in _inputtaken_
for digit in n:
    if int(digit) % 2 == 0:
        count += 1
print(count)

#if iteration needed to be done for each digit in one input use for i in n 
#if multiple inputs then use in range
#also make sure everythin is in integer
