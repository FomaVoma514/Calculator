#Фоменко Владислав
print('''Калькулятор умеет выполнять математические действия: сложение, умножение, сложение, вычитание,
возведение в степень, программа умеет конвертировать меры длины и веса, а также - переводить числа 
из различных систем счисления в дестятичную''')  # Описание того что умеет программа
print('1 - для использования калькулятора\n2 - для использования конвентера меры длины')
print('3 - для конвентера меры веса\n4 - для перевода из различных систем счисления в дестятичную')
mode = int(input('Введите цифру из вышеприведенного меню, для выбора режима: '))  # Ввод пользователем режима программы
while mode != 1 and mode != 2 and mode != 3 and mode != 4:  # Пока пользователь не введет верный номер режима
    # программа работать не будет
    mode = int(input('Введите цифру из вышеприведенного меню, для выбора режима: '))
if mode == 1:
    print('Вы выбрали режим "Калькулятор"')
    print('Калькулятор будет работать до тех пор, пока не будет введено "Стоп-слово"')
    print('Например:\nСТОП\nСтоп\nстоп')
    stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
    while stop_word != 'СТОП' and stop_word != 'Стоп' and stop_word != 'стоп':  # Программа будет выполняться пока
        # не будет введено стоп-слово
        num_1 = float(input('Введите первое число: '))  # Пользователь вводит первое число
        print('+ - сложение')
        print('-  —  вычитание')
        print('* - умножение')
        print('** - возведение в степень')
        print('/ - обыкновенное деление')
        print('// - целая часть от деления')
        print('% - остаток деления')
        operations = input('Введите операцию из меню выше для выполнения: ')
        num_2 = float(input('Введите второе число: '))  # Пользователь вводит второе число
        if operations == '+':
            print(num_1, '+', num_2, '=', num_1 + num_2)
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif operations == '-':
            print(num_1, '-', num_2, '=', num_1 - num_2)
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif operations == '*':
            print(num_1, '*', num_2, '=', num_1 * num_2)
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif operations == '**':
            print(num_1, '**', num_2, '=', num_1 ** num_2)
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif operations == '/':
            if num_2 != 0:
                print(num_1, '/', num_2, '=', num_1 / num_2)
                stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
            else:
                print('Ошибка! Деление на ноль запрещено!')
                stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif operations == '//':
            if num_2 != 0:
                print(num_1, '//', num_2, '=', num_1 // num_2)
                stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
            else:
                print('Ошибка! Деление на ноль запрещено!')
                stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif operations == '%':
            if num_2 != 0:
                print(num_1, '%', num_2, '=', num_1 % num_2)
                stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
            else:
                print('Ошибка! Деление на ноль запрещено!')
                stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
elif mode == 2:
    print('Вы выбрали режим "конвентер меры длины"')
    print('1 - миллиметры в сантиметры\n2 - миллиметры в дециметры\n3 - миллиметры в метры\n4 - миллиметры в километры')
    print('5 - сантиметры в миллиметры\n6 - сантиметры в дециметры\n7 - сантиметры в метры\n8 - сантиметры в километры')
    print('9 - дециметры в миллиметры\n10 - дециметры в сантиметры\n11 - дециметры в метры\n12 - дециметры в километры')
    print('13 - километры в миллиметры\n14 - километры в сантиметры\n15 - километры в дециметры')
    print('16 - километры в метры')
    mode_1 = int(input('Выберите режим перевода из меню выше: '))  # Пользователь вводит номер режима конвертера
    stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
    while stop_word != 'СТОП' and stop_word != 'Стоп' and stop_word != 'стоп':
        if mode_1 == 1:
            num = float(input('Введите число для перевода из миллиметров в сантиметры: '))  # Пользователь вводит число
            print(num, 'мм', '=', num / 10, 'см')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 2:
            num = float(input('Введите число для перевода из миллиметров в дециметры: '))  # Пользователь вводит число
            print(num, 'мм', '=', num / 100, 'дм')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 3:
            num = float(input('Введите число для перевода из миллиметров в метры: '))  # Пользователь вводит число
            print(num, 'мм', '=', num / 1000, 'м')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 4:
            num = float(input('Введите число для перевода из миллиметров в километры: '))  # Пользователь вводит число
            print(num, 'мм', '=', num / 1000000, 'км')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 5:
            num = float(input('Введите число для перевода из сантиметров в миллиметры: '))  # Пользователь вводит число
            print(num, 'см', '=', num * 10, 'мм')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 6:
            num = float(input('Введите число для перевода из сантиметров в дециметры: '))  # Пользователь вводит число
            print(num, 'см', '=', num / 10, 'дм')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 7:
            num = float(input('Введите число для перевода из сантиметров в метры: '))  # Пользователь вводит число
            print(num, 'см', '=', num / 100, 'м')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 8:
            num = float(input('Введите число для перевода из сантиметров в километры: '))  # Пользователь вводит число
            print(num, 'см', '=', num / 100000, 'км')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 9:
            num = float(input('Введите число для перевода из дециметров в миллиметры: '))  # Пользователь вводит число
            print(num, 'дм', '=', num * 100, 'мм')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 10:
            num = float(input('Введите число для перевода из дециметров в сантиметры: '))  # Пользователь вводит число
            print(num, 'дм', '=', num * 10, 'см')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 11:
            num = float(input('Введите число для перевода из дециметров в метры: '))  # Пользователь вводит число
            print(num, 'дм', '=', num / 10, 'м')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 12:
            num = float(input('Введите число для перевода из дециметров в километры: '))  # Пользователь вводит число
            print(num, 'дм', '=', num / 10000)
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 13:
            num = float(input('Введите число для перевода из километров в миллиметры: '))  # Пользователь вводит число
            print(num, 'км', '=', num * 1000000, 'мм')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 14:
            num = float(input('Введите число для перевода из километров в сантиметры: '))  # Пользователь вводит число
            print(num, 'км', '=', num * 100000, 'см')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 15:
            num = float(input('Введите число для перевода из километров в дециметры: '))  # Пользователь вводит число
            print(num, 'км', '=', num * 10000, 'дм')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 16:
            num = float(input('Введите число для перевода из километров в метры: '))  # Пользователь вводит число
            print(num, 'км', '=', num * 1000, 'м')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
elif mode == 3:
    print('Вы выбрали режим "конвентера меры веса"')
    print('1 - для перевода грамма в килограмм\n2 - для перевода грамма в центнер\n3 - для перевода грамма в тонну')
    print('4 - для перевода килограмма в грамм\n5 - для перевода килограмм в центнер')
    print('6 - для перевода килограмма в тонну\n7 - для перевода центнера в грамм')
    print('8 - для перевода центнера в килограмм\n9 - для перевода центнера в тонну\n10 - для перевода тонны в грамм')
    print('11 - для перевода тонны в килограмм\n12 - для перевода тонны в центнер')
    mode_1 = int(input('Выберите режим перевода из меню выше: '))  # Пользователь вводит номер режима конвертера
    stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
    while stop_word != 'СТОП' and stop_word != 'Стоп' and stop_word != 'стоп':
        if mode_1 == 1:
            num = float(input('Введите число для перевода из грамма в килограмм: '))  # Пользователь вводит число
            print(num, 'г', '=', num / 1000, 'кг')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 2:
            num = float(input('Введите число для перевода из грамма в центнер: '))  # Пользователь вводит число
            print(num, 'г', '=', num / 100000, 'ц')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 3:
            num = float(input('Введите число для перевода из грамма в тонну: '))  # Пользователь вводит число
            print(num, 'г', '=', num / 1000000, 'т')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 4:
            num = float(input('Введите число для перевода из килограмма в граммы: '))  # Пользователь вводит число
            print(num, 'кг', '=', num * 1000, 'г')
        elif mode_1 == 5:
            num = float(input('Введите число для перевода из килограмма в центнер: '))  # Пользователь вводит число
            print(num, 'кг', '=', num / 100, 'ц')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 6:
            num = float(input('Введите число для перевода из килограмма в тонну: '))  # Пользователь вводит число
            print(num, 'кг', '=', num / 1000, 'т')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 7:
            num = float(input('Введите число для перевода из центнера в граммы: '))  # Пользователь вводит число
            print(num, 'ц', '=', num * 100000, 'г')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 8:
            num = float(input('Введите число для перевода из центнера в килограммы: '))  # Пользователь вводит число
            print(num, 'ц', '=', num * 100, 'кг')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 9:
            num = float(input('Введите число для перевода из центнера в тонну: '))  # Пользователь вводит число
            print(num, 'ц', '=', num / 10, 'т')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 10:
            num = float(input('Введите число для перевода из тонны в граммы: '))  # Пользователь вводит число
            print(num, 'т', '=', num * 1000000000, 'г')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 11:
            num = float(input('Введите число для перевода из тонны в килограммы: '))  # Пользователь вводит число
            print(num, 'т', '=', num * 1000, 'кг')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
        elif mode_1 == 12:
            num = float(input('Введите число для перевода из тонны в центнеры: '))  # Пользователь вводит число
            print(num, 'т', '=', num * 10, 'ц')
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
elif mode == 4:
    print('Вы выбрали режим "перевода из одной СС в десятичную"')
    stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
    while stop_word != 'СТОП' and stop_word != 'Стоп' and stop_word != 'стоп':
        x = str(input('Введите строку или число для преобразования в десятичную СС: '))  # Пользователь вводит число
        base = int(input('Введите основание системы счисления числа "x": '))  # Пользователь вводит основание СС
        if base >= 0:
            print(int(x, base))
            stop_word = input('Если желаете продолжить, оставьте строку ввода пустой, и нажмите enter: ')
            # Конец программы
