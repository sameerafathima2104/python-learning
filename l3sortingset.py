a = int(input())
merge = set()

for i in range(a):
    first = int(input())
    second = int(input())
    merge.add(first)
    merge.add(second)

sort = sorted(merge)
total = sum(merge)

print(sort)
print(total)