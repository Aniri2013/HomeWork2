A = float(input('Введите A - '))
B = float(input('Введите B - '))
C = float(input('Введите C - '))
D = B**2 - 4 * A * C
if D < 0:
    print("решения нет")
else:
    E = D ** (1 / 2)
    F = (-B + E) / (2*A)
    G = (-B - E) / (2*A)
    if F == G :
        print ("решение есть", F)
    else :
        print (F, G)
