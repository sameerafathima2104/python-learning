words = input().split()
count = 0

for word in words:
    if word[0] == word[len(word)-1]:
        count = count + 1

print(count)