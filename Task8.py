#Data input
N = int(input("Please input any number N \n"))

#Calculation workflow
for i in range(1, N):
    flag = True
    j = 2
    while j <= i // 2:
        if i % j == 0:
            flag = False
        j += 1
    if flag == True:
        print(i)