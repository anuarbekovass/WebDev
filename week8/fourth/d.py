m = int(input())
n = input().split()
cnt = 0
result = list(map(int, n))

for i, j in enumerate(result):
    if (i >= m):
        break
    if (result[i] > result[i - 1] and i < m):
        cnt = cnt + 1

print(cnt)