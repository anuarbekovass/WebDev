n = input().split()

array = list(map(int, n))

def xor(a, b):
    if (a == b):
        return 0
    if (a or b):
        return 1

print(xor(array[0], array[1]))
