A = int(input("Введите A - "))
B = int(input("Введите B - "))
C = int(input("Введите C - "))
if A + B > C and A + C > B and B + C > A:
    print("Треугольник существует")
else:
    print("Треугольник не существует")

P = (A + B + C) / 2
print(P)