M = int(input("Введи число - "))
for i in range(1, M):
    flag = True
    j = 2
    while j <= i // 2:
        if i % j == 0:
            flag = False
        j += 1
    if flag == True:
        print(i)