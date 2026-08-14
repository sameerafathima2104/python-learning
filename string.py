s=input()
count=0
for ch in s:
    print(ch)
    if ch.lower() in "aeiou":
        count+=1
print(count)

s = input("Enter a string: ")

print("Original :", s)

print("lower()   :", s.lower())

print("upper()   :", s.upper())

print("split()   :", s.split())

print("strip()   :", s.strip())

print("replace() :", s.replace("a", "@"))

print("isalpha() :", s.isalpha())

print("isdigit() :", s.isdigit())

print("isupper() :", s.isupper())

print("islower() :", s.islower())

#lower()     -> Change to small letters

#upper()     -> Change to CAPITAL letters

#split()     -> One string → List

#strip()     -> Remove outside spaces

#replace()   -> Change one character/word

#isalpha()   -> Only alphabets?

#isdigit()   -> Only numbers?

#isupper()   -> Everything CAPITAL?

#islower()   -> Everything small?
