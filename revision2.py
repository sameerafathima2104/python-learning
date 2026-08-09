

print("36. Count Uppercase Letters")
print("37. Count Lowercase Letters")
print("38. Count Spaces")
print("39. Remove Vowels")
print("40. Reverse String")
print("41. Store Multiples of 3")
print("42. Store Multiples of 10")
print("43. Running Sum")
print("44. Running Product")
print("45. Palindrome String")
print("46. Count Positive Numbers (List)")
print("47. Count Negative Numbers (List)")
print("48. Print ASCII Values")
print("49. Character Frequency")
print("50. Unique Elements")

choice = int(input("Enter Choice : "))


if choice == 36:
    # Count Uppercase Letters

    s = input("Enter String : ")

    count = 0

    for ch in s:
        if ch.isupper():
            count += 1

    print("Uppercase Letters =", count)



elif choice == 37:
    # Count Lowercase Letters

    s = input("Enter String : ")

    count = 0

    for ch in s:
        if ch.islower():
            count += 1

    print("Lowercase Letters =", count)


elif choice == 38:
    # Count Spaces

    s = input("Enter String : ")

    count = 0

    for ch in s:
        if ch == " ":
            count += 1

    print("Spaces =", count)



elif choice == 39:
    # Remove Vowels

    s = input("Enter String : ")

    result = ""

    for ch in s:
        if ch.lower() not in "aeiou":
            result += ch

    print(result)



elif choice == 40:
    # Reverse String

    s = input("Enter String : ")

    rev = ""

    for ch in s:
        rev = ch + rev

    print(rev)



elif choice == 41:
    # Store Multiples of 3

    start = int(input("Start : "))
    end = int(input("End : "))

    result = []

    for i in range(start, end + 1):
        if i % 3 == 0:
            result.append(i)

    print(result)



elif choice == 42:
    # Store Multiples of 10

    start = int(input("Start : "))
    end = int(input("End : "))

    result = []

    for i in range(start, end + 1):
        if i % 10 == 0:
            result.append(i)

    print(result)



elif choice == 43:
    # Running Sum

    n = int(input("How many numbers? "))

    total = 0

    for i in range(n):
        num = int(input())
        total += num
        print(total)



elif choice == 44:
    # Running Product

    n = int(input("How many numbers? "))

    product = 1

    for i in range(n):
        num = int(input())
        product *= num
        print(product)



elif choice == 45:
    # Palindrome String

    s = input("Enter String : ")

    rev = ""

    for ch in s:
        rev = ch + rev

    if s == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")


elif choice == 46:
    # Count Positive Numbers in List

    n = int(input("How many numbers? "))

    count = 0

    for i in range(n):
        num = int(input())
        if num > 0:
            count += 1

    print("Positive Numbers =", count)


elif choice == 47:
    # Count Negative Numbers in List

    n = int(input("How many numbers? "))

    count = 0

    for i in range(n):
        num = int(input())
        if num < 0:
            count += 1

    print("Negative Numbers =", count)


elif choice == 48:
    # Print ASCII Values

    s = input("Enter String : ")

    for ch in s:
        print(ch, "=", ord(ch))



elif choice == 49:
    # Character Frequency

    s = input("Enter String : ")

    ch = input("Character : ")

    count = 0

    for letter in s:
        if letter == ch:
            count += 1

    print("Frequency =", count)


elif choice == 50:
    # Unique Elements

    n = int(input("How many numbers? "))

    result = []

    for i in range(n):
        num = int(input())

        if num not in result:
            result.append(num)

    print(result)



else:
    print("Invalid Choice")