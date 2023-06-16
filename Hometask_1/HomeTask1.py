#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# st2 = ''
#
# st = 'as 23 fdfdg544'
# for i in st:
#     if i.isdigit():
#         st2 += i
#
# res = ",".join(st2)
#
# print(res)

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі


# st = 'as 23 fdfdg544 34'
# new_st = ''
# for i in st:
#     if i.isdigit():
#         new_st += i
#     else:
#         new_st += ' '
#
# res = ", ".join(new_st.split())

# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
# lst = []
# for i in greeting:
#     lst.append(i.upper())
#
# print(lst)

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# lst = []
# for i in range(50):
#     if i % 2 != 0:
#         lst.append(i ** 2)
#
# print(lst)

# function
#
# - створити функцію яка виводить ліст

def show_lst(array):
    print(array)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def max_number(a, b, c):
    max_num = max(a, b, c)
    print(max_num)
    return max_num

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

def min_max(*args):
    min_num = min(args)
    max_num = max(args)
    print(max_num)
    return min_num

# - створити функцію яка повертає найбільше число з ліста

def max_of_list(array):
    max_num = max(array)
    return max_num

# - створити функцію яка повертає найменьше число з ліста

def min_of_list(array):
    min_num = min(array)
    return min_num

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def sum_of_num(array):
    sum_num = sum(array)
    return sum_num

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def avg_of_list(array):
    avg = sum(array) / len(array)
    return avg

#
#
#
#
# ################################################################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
# 3) вывести табличку множення за допомогою цикла while
# 4) переробити це завдання під меню

lst = [22, 3,5,2,8,2,-23, 8,23,5]

def del_dublicate(array):
    res = list(set(array))
    print(res)

def change_X(array):
    new_lst = []
    x = 'X'
    for index, i in enumerate(array):
        if (index + 1) % 4 == 0:
            new_lst.append('X')
        else:
            new_lst.append(i)
    print(new_lst)


def square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n-2) + '*')


def table_math():
    x = 9
    y = 1
    while y <= x:
        z = 1
        while z <= x:
            res = y * z
            print(res,  end=' ')
            if not res // 10:
                print(' ', end='')
            z = z + 1
        print('')
        y = y + 1


def main():
    while True:
        print('1) Знайти мінімальне число;')
        print('2) Видалити дублікати;')
        print('3) Замінити кожне 4-те значення на "X";')
        print('4) Вивести на екран пустий квадрат з "*";')
        print('5) Вивести табличку множення;')
        print('6) STOP;')
        res = int(input('Зробіть ваш вибір: '))

        if res == 1:
            print(min_of_list(lst))

        elif res == 2:
            del_dublicate(lst)

        elif res == 3:
            change_X(lst)

        elif res == 4:
            res2 = int(input('Введіть розмір квадрата: '))
            square(res2)

        elif res == 5:
            table_math()

        elif res == 6:
            break

main()