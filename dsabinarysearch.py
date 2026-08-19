arr = [1, 2, 4, 6, 8, 9]

target = 4

l = 0
r = len(arr) - 1

found = False

while l <= r:

    m = (l + r) // 2

    if target == arr[m]:
        print(target, m)
        found = True
        break

    if target > arr[m]:
        l = m + 1

    if target < arr[m]:
        r = m - 1

if not found:
    print(-1)


#use flag
#(l+r)//2