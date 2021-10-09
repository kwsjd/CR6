flag = True
while flag:
    try:
        a = int(input('Введите количество элементов, которые вы ходите поместить в массив: '))
    except ValueError:
            print('Вы ввели не натуральное число. Повторите попытку')
    else:
        if a <= 0:
            print('Количество элементов не может быть отрицательным')
        else:
            flag = False
flag = True
array=[]
while flag:
    try:
        for i in range(0, a):
            print(f'Введите элемент массива {i + 1}:')
            array.append(int(input()))
    except ValueError:
        print('Данный массив не может содержать что-либо кроме кроме натуральных чисел, придется Вам ввести всё заново')
    else:
        flag = False
flag = True
p = 0
while flag:
    try:
        p = int(input("введите DELTA: "))
    except ValueError:
        print('Разрешено вводить только положительные, натуральные  числа')
    else:
        if p < 0:
            print('Разрешено вводить только положительные, натуральные  числа')
        else:
            flag = False
count = array.count(min(array)+p)
print('Количество элементов в массиве, отличающихся от минимального на DELTA: ', count)