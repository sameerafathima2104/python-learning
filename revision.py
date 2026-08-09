print("1. Print 1 to n")
print("2. Print n to 1")
print("3. Print even numbers")
print("4. Print odd numbers")
print("5. Sum of first n numbers")
print("6. Factorial")
print("7. Multiplication table")
print("8. Count digits")
print("9. Sum of digits")
print("10. Reverse a number")
print("11. Count Even Digits")
print("12. Count Odd Digits")
print("13. Store Even Digits")
print("14. Store Odd Digits")

print("15. Squares in List")
print("16. Cubes in List")
print("17. Even Numbers in List")
print("18. Odd Numbers in List")

print("19. Fibonacci List")
print("20. Tribonacci List")

print("21. Count Vowels")
print("22. Count Consonants")
print("23. Remove Zeros")
print("24. Multiples of 5")
print("25. Multiples of 7")

print("26. Sum of Even Numbers")
print("27. Sum of Odd Numbers")
print("28. Largest Digit")
print("29. Smallest Digit")
print("30. Digits Divisible by 3")

print("31. Squares (Print)")
print("32. Cubes (Print)")
print("33. Count Zeros")
print("34. Alphabet Pattern")

choice=int(input("Enter Choice : "))

if choice == 1:
    n = int(input("Enter n: "))
    for i in range(1, n + 1):
        print(i)

elif choice == 2:
    n = int(input("Enter n: "))
    for i in range(n, 0, -1):
        print(i)

elif choice == 3:
    n = int(input("Enter n: "))
    for i in range(2, n + 1, 2):
        print(i)

elif choice == 4:
    n = int(input("Enter n: "))
    for i in range(1, n + 1, 2):
        print(i)

elif choice == 5:
    n = int(input("Enter n: "))
    total = 0
    for i in range(1, n + 1):
        total += i
    print("Sum =", total)

elif choice == 6:
    n = int(input("Enter n: "))
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial =", fact)

elif choice == 7:
    n = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

elif choice == 8:
    n = input("Enter a number: ")
    print("Digits =", len(n))

elif choice == 9:
    n = input("Enter a number: ")
    total = 0
    for digit in n:
        total += int(digit)
    print("Sum of digits =", total)

elif choice == 10:
    n = input("Enter a number: ")
    rev = ""
    for digit in n:
        rev = digit + rev
    print("Reverse =", rev)
#in n number operation we use range for digits we use string traversal
elif choice == 11:
    n = input("Enter a number: ")
    count = 0

    for digit in n:
        if int(digit) % 2 == 0:
            count += 1

    print("Even digits =", count)

elif choice == 12:
    n = input("Enter a number: ")
    count = 0

    for digit in n:
        if int(digit) % 2 != 0:
            count += 1

    print("Odd digits =", count)

elif choice == 13:
    n = input("Enter a number: ")

    result = []

    for digit in n:
        if int(digit) % 2 == 0:
            result.append(int(digit))

    print(result)

elif choice == 14:
    n = input("Enter a number: ")

    result = []

    for digit in n:
        if int(digit) % 2 != 0:
            result.append(int(digit))

    print(result)

elif choice == 15:
    start = int(input("Start: "))
    end = int(input("End: "))

    result = []

    for i in range(start, end + 1):
        result.append(i ** 2)

    print(result)

elif choice == 16:
    start = int(input("Start: "))
    end = int(input("End: "))

    result = []

    for i in range(start, end + 1):
        result.append(i ** 3)

    print(result)

elif choice == 17:
    start = int(input("Start: "))
    end = int(input("End: "))

    result = []

    for i in range(start, end + 1):
        if i % 2 == 0:
            result.append(i)

    print(result)

elif choice == 18:
    start = int(input("Start: "))
    end = int(input("End: "))

    result = []

    for i in range(start, end + 1):
        if i % 2 != 0:
            result.append(i)

    print(result)

elif choice == 19:
    n = int(input("Enter n: "))

    a = 0
    b = 1

    result = []

    for i in range(n):
        result.append(a)
        c = a + b
        a = b
        b = c

    print(result)

elif choice == 20:
    n = int(input("Enter n: "))

    a = 0
    b = 1
    c = 1

    result = []

    for i in range(n):
        result.append(a)
        d = a + b + c
        a = b
        b = c
        c = d

    print(result)

elif choice == 21:
    s = input("Enter a string: ")

    count = 0

    for ch in s:
        if ch.lower() in "aeiou":
            count += 1

    print(count)

elif choice == 22:
    s = input("Enter a string: ")

    count = 0

    for ch in s:
        if ch.isalpha() and ch.lower() not in "aeiou":
            count += 1

    print(count)

elif choice == 23:
    n = input("Enter number: ")

    result = []

    for digit in n:
        if digit != '0':
            result.append(int(digit))

    print(result)

elif choice == 24:
    start = int(input("Start: "))
    end = int(input("End: "))

    result = []

    for i in range(start, end + 1):
        if i % 5 == 0:
            result.append(i)

    print(result)

elif choice == 25:
    start = int(input("Start: "))
    end = int(input("End: "))

    result = []

    for i in range(start, end + 1):
        if i % 7 == 0:
            result.append(i)

    print(result)

elif choice==26:

    n=int(input("Enter n : "))

    total=0

    for i in range(2,n+1,2):
        total+=i

    print(total)

elif choice==27:

    n=int(input("Enter n : "))

    total=0

    for i in range(1,n+1,2):
        total+=i

    print(total)

elif choice==28:

    n=input("Enter Number : ")

    largest=0

    for digit in n:

        if int(digit)>largest:

            largest=int(digit)

    print(largest)

elif choice==29:

    n=input("Enter Number : ")

    smallest=9

    for digit in n:

        if int(digit)<smallest:

            smallest=int(digit)

    print(smallest)

elif choice==30:

    n=input("Enter Number : ")

    result=[]

    for digit in n:

        if int(digit)%3==0:

            result.append(int(digit))

    print(result)

elif choice==31:

    start=int(input())

    end=int(input())

    for i in range(start,end+1):

        print(i**2)

elif choice==32:

    start=int(input())

    end=int(input())

    for i in range(start,end+1):

        print(i**3)

elif choice==33:

    n=input()

    count=0

    for digit in n:

        if digit=="0":

            count+=1

    print(count)

elif choice==34:

    n=int(input())

    ch=65

    for i in range(n):

        for j in range(i+1):

            print(chr(ch),end="")

        print()

        ch+=1

else:
    print("Invalid choice")



