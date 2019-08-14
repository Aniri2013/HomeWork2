print('Введите Номер')
print('Красный = 1'
      '\nОранжевый = 2'
      '\nЖелтый = 3'
      '\nЗеленый = 4'
      '\nГолубой = 5'
      '\nСиний = 6'
      '\nФиолетовый = 7')
def is_number(strg):
    try:
        int(strg)
        if int(strg) > 0 and int(strg) <=7:
            return int(strg)
        else:
            print("Число не подходит, либо это инородный символ.")
            return False
    except ValueError:
        return False
print("Введите число: ")
A = is_number(input())
while A == False:
    print("Попытайтесь еще: ")
    A = is_number(input())

Rainbow = {
    1: {'Красный': [
    ]},

    2: {'Оранжевый': (
    )},

    3: {'Желтый': [

    ]},
    4: {'Зеленый': [

    ]},
    5: {'Голубой': [

    ]},
    6: {'Синий': [

    ]},
    7: {'Фиолетовый':
            None}
}
print(Rainbow[A])