n = input().split()
array = list(map(int, n))

def minimum(a, b, c, d):
    return min(a, b, c, d)

answer = minimum(array[0], array[1], array[2], array[3])
print(answer)