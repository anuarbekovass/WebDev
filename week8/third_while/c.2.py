n = int(input())
power = 0
i = 0
j = 1

while(j <= n):
    print(j, end = " ")
    while(i <= power):
        j *= 2
        i += 1
    power += 1

