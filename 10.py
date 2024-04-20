def combinations(k, n):
    if k == 0:
        return 1
    if k < 0 or n == 0:
        return 0
    return combinations(k - n, n - 1) + combinations(k, n - 1)


k = int(input("Введите количество кубиков K: "))
print(combinations(k, k))
