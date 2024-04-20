n = int(input('веревки'))
k = 0
while n != 0:
    n = int(input('веревки'))
    if n % 4 == 0:
        k += 1
    if n == 0:
        break
print(k)

