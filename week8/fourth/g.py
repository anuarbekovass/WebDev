m = int(input())
n = input().split()

array = list(map(int, n))

newArray = []

for i, j in enumerate(array):
    if (i < m):
        newArray.append(j)

for i in reversed(newArray):
    print(i, end=" ")