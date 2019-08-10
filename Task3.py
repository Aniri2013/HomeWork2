A = int(input("Введите A - "))
B = int(input("Введите B - "))
C = int(input("Введите C - "))
if A + B > C and A + C > B and B + C > A:
    print("Треугольник существует")
    P = (A + B + C) / 2
    S = (P * (P - A) * (P - B) * (P - C)) ** 0.5
    H1 = 2 * S / A
    H2 = 2 * S / B
    H3 = 2 * S / C
    print(max(H1, H2, H3))
else:
    print("Треугольник не существует")