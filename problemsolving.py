s=input()
count=0
for ch in s:
    ch=ch.lower()
    if ch in "aeiou":
        count=count+1
print(count)

