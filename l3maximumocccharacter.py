word = input()

count = {}

for ch in word:
    if ch in count:
        count[ch] = count[ch] + 1
    else:
        count[ch] = 1

maximum = 0

for ch in count:
    if count[ch] > maximum:
        maximum = count[ch]

for ch in count:
    if count[ch] == maximum:
        print(ch)