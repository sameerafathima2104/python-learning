n = int(input())
for i in range(n):
    ip = input()
    parts = ip.split(".")

    if len(parts) != 4:
        print("invalid")
        continue

    for part in parts:
        if not part.isdigit():
            print("invalid")
            break

        num = int(part)

        if num < 0 or num > 255:
            print("invalid")
            break

    else:
        print("valid")