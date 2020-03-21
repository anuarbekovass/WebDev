m = int(input())
n = input().split()

result = list(map(int, n))
cnt = 0

for i, j in enumerate(result):
    if (i >= m):
        break
    if (i == 0 or i == m-1):
        continue
    if (result[i-1] < result[i] and result[i] > result[i+1]):
        cnt += 1

print(cnt)