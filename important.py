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
#Time Complexity O(n) — one pass through all digits. Space Complexity O(1) — only a counter is used.
a = int(input())
count = 0

while a != 0:
    digit = a % 10      # Get last digit

    if digit % 2 == 0:
        count += 1

    a = a // 10         # Remove last digit

print(count)

#other method
#Whenever a question involves digits of a number, try to solve it both ways:String traversal (input() and for digit in n)
#Mathematical approach (% 10 and // 10)