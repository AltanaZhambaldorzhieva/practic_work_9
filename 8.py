def count_ways(x):
    count = 0

    for i in range(1, int(x ** 0.5) + 1):
        j = int((x - i ** 2) ** 0.5)
        if i ** 2 + j ** 2 == x and i <= j:
            count += 1

    return count


x = int(input())
ways = count_ways(x)
print(ways)
