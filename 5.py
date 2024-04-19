def palindrome(num):
    return str(num) == str(num)[::-1]


for mileage in range(100000, 999999):

    if palindrome(mileage % 100000) and palindrome(mileage % 10000 // 10) and \
            palindrome(mileage):
        print("Пробег:", mileage)
        break
