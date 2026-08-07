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

choice = int(input("Enter your choice (1-10): "))

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

else:
    print("Invalid choice")


#in n number operation we use range for digits we use string traversal