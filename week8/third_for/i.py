import math

x = int(input())
counter = 0

for i in range(1, int(math.sqrt(x))):
    if(x % i == 0):
        counter = counter + 1

counter = counter * 2

print(counter)