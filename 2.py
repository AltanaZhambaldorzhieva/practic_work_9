n = int(input('число большее чем 2'))
while n**0.5 > 2:
    print(round(n**0.5, 3))
    n = n**0.5
    if n**0.5 <= 2:
        print(round(n**0.5, 3))
        break



