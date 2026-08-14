r = int(input())
c = int(input())

A = []
B = []

print("Matrix A")
for i in range(r):
    A.append(list(map(int, input().split())))

print("Matrix B")
for i in range(r):
    B.append(list(map(int, input().split())))

result = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    result.append(row)

for row in result:
    print(*row)