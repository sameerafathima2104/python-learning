print("1. Count Vowels")
print("2. Store Even Digits")
print("3. Count Uppercase Letters")
print("4. Store Vowels")
print("5. Store Consonants")
print("6. Store Even Squares")
print("7. Number and Square Tuples")
print("8. Character and ASCII Tuples")
print("9. Unique Characters")

choice = int(input("Enter your choice (1-9): "))

if choice == 1:
    s = input("Enter a string: ")
    count = 0
    for ch in s:
        if ch.lower() in "aeiou":
            count += 1
    print(count)

elif choice == 2:
    s = input("Enter a number: ")
    even = []
    for ch in s:
        if int(ch) % 2 == 0:
            even.append(int(ch))
    print(even)

elif choice == 3:
    s = input("Enter a string: ")
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1
    print(count)

elif choice == 4:
    s = input("Enter a string: ")
    vowels = []
    for ch in s:
        if ch.lower() in "aeiou":
            vowels.append(ch)
    print(vowels)

elif choice == 5:
    s = input("Enter a string: ")
    consonants = []
    for ch in s:
        if ch.isalpha() and ch.lower() not in "aeiou":
            consonants.append(ch)
    print(consonants)

elif choice == 6:
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))
    squares = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            squares.append(i * i)
    print(squares)

elif choice == 7:
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))

    if start > end:
        print("Invalid Range")
    else:
        result = []
        for i in range(start, end + 1):
            result.append((i, i * i))
        print(result)

elif choice == 8:
    s = input("Enter a string: ")
    result = []
    for ch in s:
        result.append((ch, ord(ch)))
    print(result)

elif choice == 9:
    s = input("Enter a string: ")
    unique = []
    for ch in s:
        if ch not in unique:
            unique.append(ch)
    print(unique)

else:
    print("Invalid Choice")