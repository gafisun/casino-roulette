# ========== Импорт библиотек ========== #
import random
import plotly.graph_objs as go
import shutil
import requests
from PIL import Image
# TODO: Добавить комментарии к каждой функции
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# ========== Функция сброса значений всех начальных переменных ========== #
def reset():
    global start_money
    global k
    global sum_black
    global sum_red
    global sum_zero
    global mode
    global mode_mode
    global select_one
    global select_two
    global select_three
    global select_four
    global select_six
    global select_twelve_dozen
    global  select_twelve_column
    start_money = 100000
    k = 0.001
    sum_black = 18
    sum_red = 18
    sum_zero = 1
    mode = 'На число'
    mode_mode = ''
    select_one = -1
    select_two = []
    select_three = []
    select_four = []
    select_six = []
    select_twelve_dozen = []
    select_twelve_column = []


# ========== Функция сброса значений количества фишек========== #
def reset_sum():
    global sum_black
    global sum_red
    global sum_zero
    sum_black = 18
    sum_red = 18
    sum_zero = 1


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# ========== Инцилизация постоянных переменных ========== #
f = 0
red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)
black = (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)
split_list = ([0, 1], [0, 2], [0, 3], [1, 0], [1, 2], [1, 4], [2, 0], [2, 1], [2, 3],
              [2, 5], [3, 0], [3, 2], [3, 6], [4, 1], [4, 5], [4, 7], [5, 4], [5, 2],
              [5, 6], [5, 8], [7, 4], [7, 8], [7, 10], [8, 7], [8, 5], [8, 9], [8, 11],
              [9, 8], [9, 6], [9, 12], [10, 13], [10, 7], [10, 11], [11, 10], [11, 8],
              [11, 12], [11, 14], [12, 11], [12, 9], [12, 15], [13, 16], [13, 10], [13, 14],
              [14, 13], [14, 11], [14, 15], [14, 17], [15, 18], [15, 14], [15, 12], [16, 19],
              [16, 17], [16, 13], [17, 16], [17, 14], [17, 18], [17, 20], [18, 21], [18, 17],
              [18, 15], [19, 22], [19, 20], [19, 16], [20, 19], [20, 17], [20, 21], [20, 23],
              [21, 24], [21, 20], [21, 18], [22, 25], [22, 23], [22, 19], [23, 26], [23, 22],
              [23, 20], [23, 24], [24, 27], [24, 23], [24, 21], [25, 28], [25, 26], [25, 22],
              [26, 29], [26, 25], [26, 23], [26, 27], [27, 30], [27, 26], [27, 24], [28, 31],
              [28, 29], [28, 25], [29, 32], [29, 28], [29, 26], [29, 30], [30, 33], [30, 29],
              [30, 27], [31, 34], [31, 32], [31, 28], [32, 35], [32, 31], [32, 29], [32, 33],
              [33, 36], [33, 32], [33, 30], [34, 35], [34, 31], [35, 34], [35, 32], [35, 36],
              [36, 35], [36, 33])
# TODO: Убрать ненужные пары чисел
street_list = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15],
               [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27],
               [28, 29, 30], [31, 32, 33], [34, 35, 36])
square_list = ([1, 2, 4, 5], [4, 5, 7, 8], [7, 8, 10, 11], [10, 11, 13, 14], [13, 14, 16, 17],
               [16, 17, 19, 20], [19, 20, 22, 23], [22, 23, 25, 26], [25, 26, 28, 29], [28, 29, 31, 32],
               [31, 32, 34, 35], [2, 3, 5, 6], [5, 6, 8, 9], [8, 9, 12, 13], [11, 12, 14, 15],
               [14, 15, 17, 18], [17, 18, 20, 21], [20, 21, 23, 24], [23, 24, 26, 27],
               [26, 27, 29, 30], [29, 30, 32, 33], [32, 33, 35, 36])
double_street_list = ([1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9], [7, 8, 9, 10, 11, 12],
                      [10, 11, 12, 13, 14, 15], [13, 14, 15, 16, 17, 18], [16, 17, 18, 19, 20, 21],
                      [19, 20, 21, 22, 23, 24], [22, 23, 24, 25, 26, 27], [25, 26, 27, 28, 29, 30],
                      [28, 29, 30, 31, 32, 33], [31, 32, 33, 34, 35, 36])
dozen_list = {1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2: [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 3: [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]}
column_list = {1: [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34], 2: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35], 3: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]}
mode_list = ("На число", "Сплит", "Стрит", "Угол", "Двойной Стрит", "Дюжина", "Колонна", "Равные числа")
mode_mode_list = ("Чёрное", "Красное", "Чётное", "Нечётное", "Меньше", "Больше")
random_picture = random.random()
my_url = 'https://static.vecteezy.com/system/resources/previews/000/155/653/original/green-roulette-table-vector.jpg'

reset()


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# ========== Функция показа значений изменяемых переменных ========== #
def show_arg():
    global select_one
    global select_two
    global select_three
    global square_four
    global mode_mode

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print(start_money, '\033[93m' + '<-начальная сумма денег' + '\033[0m')
    print(k, '\033[93m' + '<-начальный коэффицент ставок' + '\033[0m')
    print((start_money * k), '\033[93m' + '<-начальная сумма ставок' + '\033[0m')
    print(sum_black, '\033[93m' + '<-начальное количество чёрных ячеек' + '\033[0m')
    print(sum_red, '\033[93m' + '<-начальное количество белых ячеек' + '\033[0m')
    print(sum_zero, '\033[93m' + '<-начальное количество ячейки "зиро"' + '\033[0m')
    print(mode, '\033[93m' + '<-режим игры' + '\033[0m')
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    # ========== ==========
    if len(mode_mode) != 0 and mode == 'Равные числа':
        print(mode_mode, '\033[93m' + '<-Тип режима игры "Равные числа"' + '\033[0m')
    elif len(mode_mode) == 0 and mode == 'Равные числа':
        print('Тип режима игры "Равные числа" ', '\033[91m' + 'не выбран!' + '\033[0m')
    # ========== ==========
    if select_one > -1 and mode == 'На число':
        print(select_one, '\033[93m' + '<-Выбранное число для режима игры "На число"' + '\033[0m')
    elif select_one == -1 and mode == 'На число':
        print('Единственное число для режима игры "На число"', '\033[91m' + 'не выбрано!' + '\033[0m')
    # ========== ==========
    if len(select_two) > 0 and mode == 'Сплит':
        print(str(select_two[0]) + ',' + str(select_two[1]),
              '\033[93m' + '<-Выбранная двойка чисел для режима игры "Сплит"' + '\033[0m')
    elif len(select_two) == 0 and mode == 'Сплит':
        print('Двойка чисел для режима игры "Стрит"', '\033[91m' + 'не выбрана!' + '\033[0m')
    # ========== ==========
    if len(str(select_three)) > 2 and mode == 'Стрит':
        print(str(*select_three[0:1]) + ',' + str(*select_three[1:2]) + ',' + str(*select_three[2:3]),
              '\033[93m' + '<-Выбранная тройка чисел для режима игры "Стрит"' + '\033[0m')
    elif len(str(select_three)) == 0 and mode == 'Стрит':
        print('Тройка чисел для режима игры "Стрит"', '\033[91m' + 'не выбрана!' + '\033[0m')
    # ========== ==========
    if len(str(select_four)) > 2 and mode == 'Угол':
        print(str(*select_four[0:1]) + ',' + str(*select_four[1:2]) + ',' + str(*select_four[2:3]) + ',' + str(
            *select_four[3:4]), '\033[93m' + '<-Выбранная четвёрка чисел для режима игры "Угол"' + '\033[0m')
    elif len(str(select_four)) == 1 and mode == 'Угол':
        print('Четвёрка чисел для режима игры "Угол"', '\033[91m' + 'не выбрана!' + '\033[0m')


# ========== Функция вывода заключительного блока с текстом ========== #
def text_end():
    print(' ')
    print('\033[96m' + '<Хотите, что-нибудь ЕЩЁ изменить?>' + '\033[0m')
    print('\033[92m' + '•Если нет, то погнали! Пиши команду "run" и смотри на результат!' + '\033[0m')
    print(' ')
    print('\033[92m' + '•Если да, то напиши команду "help" для вывода всех команд.' + '\033[0m')


show_arg()


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# ========== Функции по выводу справочной информации о всевозможных командах ========== #
def help():
    print('show_arg', '\033[93m' + '<-Вывод списка начальных значений' + '\033[0m')
    print('show_board', '\033[93m' + '<-Показ игровой доски для ставок' + '\033[0m')
    print('set_black', '\033[93m' + '<-Задать количество чёрных фишек' + '\033[0m')
    print('set_red', '\033[93m' + '<-Задать количество белых фишек' + '\033[0m')
    print('set_zero', '\033[93m' + '<-Задать количество фишек "зиро"' + '\033[0m')
    print('set_k', '\033[93m' + '<-Задать коэффицент ставок' + '\033[0m')
    print('set_money', '\033[93m' + '<-Задать начальную сумму денег' + '\033[0m')
    print('set_mode', '\033[93m' + '<-Задать режим игры' + '\033[0m')
    print('reset', '\033[93m' + '<-Сброс до значений по умолчанию' + '\033[0m')
    print('stop', '\033[93m' + '<-Выйти из игры' + '\033[0m')
    print('help', '\033[93m' + '<-Вывод всех команд' + '\033[0m')
    print('help_mode', '\033[93m' + 'Вывод все возможных режимов игры и их подтипов' + '\033[0m')
    # TODO: Добавить команду смены типа рулетки: Американская на Европейскую


# ========== Функция по выводу справочной информации о всевозможных режимах и типах игры========== #
def help_mode():
    print('На число',
          '\033[93m' + '<-Ставка на одно выбранное вами число. В случае победы возвращается ставка * 36.' + '\033[0m')
    print('Сплит',
          '\033[93m' + '<-Ставка на 2 выбранных вами числа, ячейки которых имеют общую грань. В случае победы возвращается ставка * 18.' + '\033[0m')
    print('Стрит',
          '\033[93m' + '<-Ставка на 3 выбранных вами числа, ячейки которых выстраиваются в один столбец. В случае победы возвращается ставка * 12.' + '\033[0m')
    print('Угол',
          '\033[93m' + '<-Ставка на 4 выбранных вами числа, ячейки которых имеют общую вершину. В случае победы возвращается ставка * 9.' + '\033[0m')
    print('Двойной Стрит',
          '\033[93m' + '<-Ставка на 6 выбранных вами чисел, ячейки которых имеют выстраиваются в два столбца, которые соприкасаются друг с другом. В случае победы возвращается ставка * 6.' + '\033[0m')
    print('Дюжина',
          '\033[93m' + '<-Ставка на 12 выбранных вами чисел. Возможные группы: от 1 до 12, от 13 до 24, от 25 до 36  В случае победы возвращается ставка * 3.' + '\033[0m')
    print('Колонна',
          '\033[93m' + '<-Ставка на 12 выбранных вами чисел. Возможные группы: от 1 до 12,  от 13 до 24, от 25 до 36  В случае победы возвращается ставка * 3.' + '\033[0m')
    print('Равные числа',
          '\033[93m' + '<-Ставка на половину ячеек по определённому признаку (не включая "зиро"). В случае победы возвращается ставка * 2.' + '\033[0m')
    print('\033[94m' + '             •Чёрное' + '\033[0m', '\033[93m' + '<-Ставка на ячейки чёрного цвета.' + '\033[0m')
    print('\033[94m' + '             •Красное' + '\033[0m',
          '\033[93m' + '<-Ставка на ячейки красного цвета.' + '\033[0m')
    print('\033[94m' + '             •Чётное' + '\033[0m',
          '\033[93m' + '<-Ставка на ячейки с чётным номером.' + '\033[0m')
    print('\033[94m' + '             •Нечётное' + '\033[0m',
          '\033[93m' + '<-Ставка на ячейки с нечётном номером.' + '\033[0m')
    print('\033[94m' + '             •Меньше' + '\033[0m',
          '\033[93m' + '<-Ставка на ячейки с 1 по 17 (включительно).' + '\033[0m')
    print('\033[94m' + '             •Больше' + '\033[0m',
          '\033[93m' + '<-Ставка на ячейки с 18 по 36 (включительно).' + '\033[0m')


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# ========== Функция настройки начального количества чёрных фишек ========== #
def set_black():
    global sum_black
    print('\033[90m' + 'Вводи ,пожалуйста, только числовое значение, иначе всё сломается(' + '\033[0m')
    d = 0
    while d == 0:
        i = int(input())
        if i > 37 or i <= 0:
            print(
                '\033[91m' + 'Введи значение не больше, чем число возможных ячеек (36), а также не меньше нуля!' + '\033[0m')
        else:
            sum_black = i
            print('Начальное количество чёрных ячеек изменено на :', '\033[93m' + str(sum_black) + '\033[0m')
            d += 1

        text_end()


# ========== Функция настройки начального количества красных фишек ========== #
def set_red():
    global sum_red
    print('\033[90m' + 'Вводи ,пожалуйста, только числовое значение, иначе всё сломается(' + '\033[0m')
    d = 0
    while d == 0:
        i = int(input())
        if i > 37 or i <= 0:
            print(
                '\033[91m' + 'Введи значение не больше, чем число возможных ячеек (36), а также не меньше нуля!' + '\033[0m')
        else:
            sum_red = i
            print('Начальное количество красных ячеек изменено на :', '\033[93m' + str(sum_red) + '\033[0m')
            d += 1
    text_end()


# ========== Функция настройки начального количества "зиро" фишек ========== #
def set_zero():
    global sum_zero
    print('\033[90m' + 'Вводи ,пожалуйста, только числовое значение, иначе всё сломается(' + '\033[0m')
    d = 0
    while d == 0:
        i = int(input())
        if i < 0 or i > 1:
            print(
                '\033[91m' + 'Введи значение не больше, чем число возможных фишек (1), а также не меньше нуля!' + '\033[0m')
        else:
            sum_zero = i
            print('Начальное количество "зиро" ячеек изменено на :', '\033[93m' + str(sum_zero) + '\033[0m')
            d += 1
    text_end()


# ========== Функция настройки начального коэффицента ставок ========== #
def set_k():
    global k
    print('\033[90m' + 'Вводи ,пожалуйста, только числовое значение от 0 до 1, иначе всё сломается(' + '\033[0m')
    d = 0
    while d == 0:
        i = float(input())
        if i < 0 or i >= 1:
            print(
                '\033[91m' + 'Введи значение не больше, чем число возможных фишек (30), а также не меньше нуля!' + '\033[0m')
        else:
            k = i
            print('Начальный коэффицент ставок изменён на:', '\033[93m' + str(k) + '\033[0m')
            d += 1
    text_end()


# ========== Функция настройки начального количества денежных средств ========== #
def set_money():
    global start_money
    print('\033[90m' + 'Вводи ,пожалуйста, только числовое значение от 0 до 1, иначе всё сломается(' + '\033[0m')
    d = 0
    while d == 0:
        i = int(input())
        if i < 0:
            print('\033[91m' + 'Введи значение не меньше нуля!' + '\033[0m')
        else:
            start_money = i
            print('Начальное количество денег изменено на:', '\033[93m' + str(start_money) + '\033[0m')
            d += 1
    text_end()


# ========== Функция настройки режима игры ========== #
def set_mode():
    global mode
    print('\033[90m' + 'Все возможные режимы игры и их подтипы можно узнать по команде "help_mode"' + '\033[0m')
    d = 0
    while d == 0:
        i = input()
        if i not in mode_list:
            print('\033[91m' + 'Такого режима игры нет( Введите существующий!' + '\033[0m')
        else:
            mode = i
            print('Режим игры изменён на :', '\033[93m' + str(mode) + '\033[0m')
            d += 1
    text_end()


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# ========== Пасхалка для тех, кому очень грустно ========== #
def positive():
    global my_url
    my_url = 'https://bipbap.ru/wp-content/uploads/2017/12/tmp754047087187853313.jpg'
    show_board()
    print('\033[91m' + 'Оставайся всегда позитивным!' + '\033[0m')


# ========== Функция прерывания программы========== #
def stop():
    global c
    print('\033[91m' + 'Буду рад предсказать игру ещё раз! До встречи!' + '\033[0m')


# ========== Функция заглушка, необходимая для случаев, когда вводится неправильная или несуществующая команда========== #
def mistake():
    print('\033[91m' + 'Такой команды нет(' + '\033[0m')
    print('\033[92m' + 'Напиши команду "help_list" для вывода всех команд, если ты вдруг их забыл.' + '\033[0m')
    print('\033[92m' + 'Для выхода из игры, напиши команду "stop".' + '\033[0m')


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# ========== Функции закачки из сети и вывода изображения игральной доски ========== #
def show_board():
    response = requests.get(my_url, stream=True)
    with open(str(random_picture) + '.png', 'wb') as file:
        shutil.copyfileobj(response.raw, file)
    del response
    img = Image.open(str(random_picture) + '.png')
    img.show()
    text_end()


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# ========== Функции выбора и работы для режима игры НА ЧИСЛО ========== #
def one_pos_select():
    global select_one
    print('\033[96m' + 'Вы выбрали режим "На число". Введите далее число, на которое вы ставите!' + '\033[0m')
    print('\033[90m' + 'Вводи ,пожалуйста, только числовое значение от 0 до 36, иначе всё сломается(' + '\033[0m')
    print(
        '\033[90m' + 'Кроме этого, не забывайте, что количества фишек сбрасываются до значений по умолчанию.' + '\033[0m')
    reset_sum()
    d = 0
    while d == 0:
        i = int(input())
        if i > 36 or i < 0:
            print(
                '\033[91m' + 'Введи значение не больше, чем число возможных ячеек (38), а также не меньше нуля!' + '\033[0m')
        else:
            select_one = i
            d += 1


def one_pos():
    win = 0
    loose = 0
    balance = []
    batch = []
    money = start_money
    while money > 0:
        bid = start_money * k

        if bid > money:
            bid = money

        money -= bid

        balance.append(money)
        batch.append(len(batch) + 1)

        sum_arg = sum_black + sum_red + sum_zero
        ball = random.randint(0, sum_arg - 1)

        if ball == select_one:
            money += bid * 36
            win += 1
        else:
            loose += 1
        if (win + loose) >= 100000:
            money = 0
    games = win + loose
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    show_arg()
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(
        win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(
        loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance, mode='lines', line=dict(color='purple', width=3)))
    fig.update_layout(title=dict(text=str(mode)))
    fig.update_xaxes(title_text='Количество сыгранных партий')
    fig.update_yaxes(title_text='Количество денежных средств')
    fig.show()


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# ========== Функции выбора и работа для каждого типа режима игры РАВНЫЕ ЧИСЛА ========== #
def half_pos_select():
    global mode_mode
    print('\033[96m' + 'Уточните тип игры "Равные числа"!' + '\033[0m')
    d = 0
    while d == 0:
        mode_mode = input()
        if mode_mode in mode_mode_list:
            print('Режим игры изменён на: ', mode + " " + mode_mode)
            d += 1
        elif mode_mode != 'help_mode':
            print('\033[91m' + 'Такого подтипа режима игры "Равные числа "нет(' + '\033[0m')
            print('\033[93m' + 'Все возможные режимы игры и их подтипы можно узнать по команде "help_mode"' + '\033[0m')
        else:
            help_mode()


# ========== Функции выбора и работа для  типа режима игры РАВНЫЕ ЧИСЛА_ЧЁРНОЕ========== #
def half_pos_black():
    win = 0
    loose = 0
    balance = []
    batch = []
    money = start_money
    while money > 0:
        bid = start_money * k

        if bid > money:
            bid = money

        money -= bid

        balance.append(money)
        batch.append(len(batch) + 1)

        sum_arg = sum_black + sum_red + sum_zero
        ball = random.randint(1, sum_arg)

        if ball in black:
            money += bid * 2
            win += 1
        else:
            loose += 1
        if (win + loose) >= 100000:
            money = 0
    games = win + loose
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    show_arg()
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(
        win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(
        loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance, mode='lines', line=dict(color='purple', width=3)))
    fig.update_layout(title=dict(text=str(mode)))
    fig.update_xaxes(title_text='Количество сыгранных партий')
    fig.update_yaxes(title_text='Количество денежных средств')
    fig.show()


# ========== Функции выбора и работа для  типа режима игры РАВНЫЕ ЧИСЛА_КРАСНОЕ========== #
def half_pos_red():
    win = 0
    loose = 0
    balance = []
    batch = []
    money = start_money
    while money > 0:
        bid = start_money * k

        if bid > money:
            bid = money

        money -= bid

        balance.append(money)
        batch.append(len(batch) + 1)

        sum_arg = sum_black + sum_red + sum_zero
        ball = random.randint(1, sum_arg)

        if ball in red:
            money += bid * 2
            win += 1
        else:
            loose += 1
        if (win + loose) >= 100000:
            money = 0
    games = win + loose
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    show_arg()
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(
        win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(
        loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance, mode='lines', line=dict(color='purple', width=3)))
    fig.update_layout(title=dict(text=str(mode)))
    fig.update_xaxes(title_text='Количество сыгранных партий')
    fig.update_yaxes(title_text='Количество денежных средств')
    fig.show()
    
    
# ========== Функции выбора и работа для  типа режима игры РАВНЫЕ ЧИСЛА_ЧЁТНОЕ========== #
def half_pos_even():
    win = 0
    loose = 0
    balance = []
    batch = []
    money = start_money
    while money > 0:
        bid = start_money * k

        if bid > money:
            bid = money

        money -= bid

        balance.append(money)
        batch.append(len(batch) + 1)

        sum_arg = sum_black + sum_red + sum_zero
        ball = random.randint(1, sum_arg)

        if (ball % 2) == 0:
            money += bid * 2
            win += 1
        else:
            loose += 1
        if (win + loose) >= 100000:
            money = 0
    games = win + loose
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    show_arg()
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(
        win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(
        loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance, mode='lines', line=dict(color='purple', width=3)))
    fig.update_layout(title=dict(text=str(mode)))
    fig.update_xaxes(title_text='Количество сыгранных партий')
    fig.update_yaxes(title_text='Количество денежных средств')
    fig.show()


# ========== Функции выбора и работа для  типа режима игры РАВНЫЕ ЧИСЛА_НЕЧЁТНОЕ========== #
def half_pos_odd():
    win = 0
    loose = 0
    balance = []
    batch = []
    money = start_money
    while money > 0:
        bid = start_money * k

        if bid > money:
            bid = money

        money -= bid

        balance.append(money)
        batch.append(len(batch) + 1)

        sum_arg = sum_black + sum_red + sum_zero
        ball = random.randint(1, sum_arg)

        if (ball % 2) != 0:
            money += bid * 2
            win += 1
        else:
            loose += 1
        if (win + loose) >= 100000:
            money = 0
    games = win + loose
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    show_arg()
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(
        win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(
        loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance, mode='lines', line=dict(color='purple', width=3)))
    fig.update_layout(title=dict(text=str(mode)))
    fig.update_xaxes(title_text='Количество сыгранных партий')
    fig.update_yaxes(title_text='Количество денежных средств')
    fig.show()


# ========== Функции выбора и работа для  типа режима игры РАВНЫЕ ЧИСЛА_БОЛЬШЕ========== #
def half_pos_big():
    win = 0
    loose = 0
    balance = []
    batch = []
    money = start_money
    while money > 0:
        bid = start_money * k

        if bid > money:
            bid = money

        money -= bid

        balance.append(money)
        batch.append(len(batch) + 1)

        sum_arg = sum_black + sum_red + sum_zero
        ball = random.randint(1, sum_arg)

        if ball >= 18:
            money += bid * 2
            win += 1
        else:
            loose += 1
        if (win + loose) >= 100000:
            money = 0
    games = win + loose
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    show_arg()
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(
        win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(
        loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance, mode='lines', line=dict(color='purple', width=3)))
    fig.update_layout(title=dict(text=str(mode)))
    fig.update_xaxes(title_text='Количество сыгранных партий')
    fig.update_yaxes(title_text='Количество денежных средств')
    fig.show()


# ========== Функции выбора и работа для  типа режима игры РАВНЫЕ ЧИСЛА_МЕНЬШЕ========== #
def half_pos_small():
    win = 0
    loose = 0
    balance = []
    batch = []
    money = start_money
    while money > 0:
        bid = start_money * k

        if bid > money:
            bid = money

        money -= bid

        balance.append(money)
        batch.append(len(batch) + 1)

        sum_arg = sum_black + sum_red + sum_zero
        ball = random.randint(1, sum_arg)

        if ball <= 18:
            money += bid * 2
            win += 1
        else:
            loose += 1
        if (win + loose) >= 100000:
            money = 0
    games = win + loose
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    show_arg()
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(
        win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(
        loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance, mode='lines', line=dict(color='purple', width=3)))
    fig.update_layout(title=dict(text=str(mode)))
    fig.update_xaxes(title_text='Количество сыгранных партий')
    fig.update_yaxes(title_text='Количество денежных средств')
    fig.show()


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# ========== Функция выбора и работы для режима игры СПЛИТ ========== #
def split_select():
    global select_two
    print(
        '\033[96m' + 'Вы выбрали режим "Сплит". Введите далее 2 числа, нарисованные рядом друг с другом на поле, на которое вы ставите!' + '\033[0m')
    print('\033[90m' + 'Вводи ,пожалуйста, только числовые значения от 0 до 36, иначе всё сломается(' + '\033[0m')
    print(
        '\033[90m' + 'Кроме этого, не забывайте, что количества фишек сбрасываются до значений по умолчанию.' + '\033[0m')
    reset_sum()
    d = 0
    while d == 0:
        a, b = map(int, input().split())
        select_two.append(a)
        select_two.append(b)
        if select_two in split_list:
            print('Вы выбрали следующую пару', str(select_two[0]) + ',' + str(select_two[1]))
            break
        else:
            print('\033[91m' + 'Вы не можете поставить ставку на такую пару ячеек.' + '\033[0m')


def split():
    win = 0
    loose = 0
    balance = []
    batch = []
    money = start_money
    while money > 0:
        bid = start_money * k

        if bid > money:
            bid = money

        money -= bid

        balance.append(money)
        batch.append(len(batch) + 1)

        sum_arg = sum_black + sum_red + sum_zero
        ball = random.randint(1, sum_arg)

        if ball in select_two:
            money += bid * 18
            win += 1
        else:
            loose += 1
        if (win + loose) >= 100000:
            money = 0
    games = win + loose
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    show_arg()
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(
        win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(
        loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance, mode='lines', line=dict(color='purple', width=3)))
    fig.update_layout(title=dict(text=str(mode)))
    fig.update_xaxes(title_text='Количество сыгранных партий')
    fig.update_yaxes(title_text='Количество денежных средств')
    fig.show()


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# ========== Функции выбора и работы для режима игры СТРИТ ========== #
def street_select():
    global select_three
    print(
        '\033[96m' + 'Вы выбрали режим "Стрит". Введите далее 3 числа, которые нарисованы в один столбец на поле, на которые вы ставите!' + '\033[0m')
    print('\033[90m' + 'Вводи ,пожалуйста, только числовые значения от 1 до 36, иначе всё сломается(' + '\033[0m')
    print(
        '\033[90m' + 'Кроме этого, не забывайте, что количества фишек сбрасываются до значений по умолчанию.' + '\033[0m')
    reset_sum()
    d = 0
    while d == 0:
        a, b, c = map(int, input().split())
        select_three.append(a)
        select_three.append(b)
        select_three.append(c)
        select_three.sort()
        if select_three in street_list:
            print('Вы выбрали следующую пару',
                  str(select_three[0]) + ',' + str(select_three[1]) + ',' + str(select_three[2]))
            break
        else:
            print('\033[91m' + 'Вы не можете поставить ставку на такую тройку ячеек.' + '\033[0m')


def street():
    win = 0
    loose = 0
    balance = []
    batch = []
    money = start_money
    while money > 0:
        bid = start_money * k

        if bid > money:
            bid = money

        money -= bid

        balance.append(money)
        batch.append(len(batch) + 1)

        sum_arg = sum_black + sum_red + sum_zero
        ball = random.randint(0, sum_arg - 1)

        if ball in select_three:
            money += bid * 12
            win += 1
        else:
            loose += 1
        if (win + loose) >= 100000:
            money = 0
    games = win + loose
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    show_arg()
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(
        win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(
        loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance, mode='lines', line=dict(color='purple', width=3)))
    fig.update_layout(title=dict(text=str(mode)))
    fig.update_xaxes(title_text='Количество сыгранных партий')
    fig.update_yaxes(title_text='Количество денежных средств')
    fig.show()


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# Функции выбора и работы для режима игры УГОЛ ========== #
def square_select():
    global select_four
    print(
        '\033[96m' + 'Вы выбрали режим "Угол". Введите далее 4 числа, ячейки которых имеют общую вершину , на которые вы ставите!' + '\033[0m')
    print('\033[90m' + 'Вводи ,пожалуйста, только числовые значения от 1 до 36, иначе всё сломается(' + '\033[0m')
    print(
        '\033[90m' + 'Кроме этого, не забывайте, что количества фишек сбрасываются до значений по умолчанию.' + '\033[0m')
    reset_sum()
    d = 0
    while d == 0:
        a, b, c, d = map(int, input().split())
        select_four.append(a)
        select_four.append(b)
        select_four.append(c)
        select_four.append(d)
        select_four.sort()
        if select_four in square_list:
            print('Вы выбрали следующую пару',
                  str(select_four[0]) + ',' + str(select_four[1]) + ',' + str(select_four[2]) + ',' + str(select_four[3]))
            break
        else:
            print('\033[91m' + 'Вы не можете поставить ставку на такую четвёрку ячеек.' + '\033[0m')


def square():
    win = 0
    loose = 0
    balance = []
    batch = []
    money = start_money
    while money > 0:
        bid = start_money * k

        if bid > money:
            bid = money

        money -= bid

        balance.append(money)
        batch.append(len(batch) + 1)

        sum_arg = sum_black + sum_red + sum_zero
        ball = random.randint(0, sum_arg - 1)

        if ball in select_four:
            money += bid * 9
            win += 1
        else:
            loose += 1
        if (win + loose) >= 100000:
            money = 0
    games = win + loose
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    show_arg()
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(
        win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(
        loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance, mode='lines', line=dict(color='purple', width=3)))
    fig.update_layout(title=dict(text=str(mode)))
    fig.update_xaxes(title_text='Количество сыгранных партий')
    fig.update_yaxes(title_text='Количество денежных средств')
    fig.show()


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# ========== Функции выбора и работы для режима игры ДВОЙНОЙ СТРИТ ==========
def double_street_select():
    global select_six
    print(
        '\033[96m' + 'Вы выбрали режим "Стрит". Введите далее 6 чисел, ячейки которых нарисованы в два столбца на поле, на которые вы ставите!' + '\033[0m')
    print('\033[90m' + 'Вводи ,пожалуйста, только числовые значения от 1 до 36, иначе всё сломается(' + '\033[0m')
    print(
        '\033[90m' + 'Кроме этого, не забывайте, что количества фишек сбрасываются до значений по умолчанию.' + '\033[0m')
    reset_sum()
    d = 0
    while d == 0:
        a, b, c, d, e, g = map(int, input().split())
        select_six.append(a)
        select_six.append(b)
        select_six.append(c)
        select_six.append(d)
        select_six.append(e)
        select_six.append(g)
        select_six.sort()
        if select_six in double_street_list:
            print('Вы выбрали следующую пару',
                  str(select_six[0]) + ',' + str(select_six[1]) + ',' + str(select_six[2]) + ',' + str(
                      select_six[3]) + ',' + str(select_six[4]) + ',' + str(select_six[5]))
            break
        else:
            print('\033[91m' + 'Вы не можете поставить ставку на такую шестёрку ячеек.' + '\033[0m')


def double_street():
    win = 0
    loose = 0
    balance = []
    batch = []
    money = start_money
    while money > 0:
        bid = start_money * k

        if bid > money:
            bid = money

        money -= bid

        balance.append(money)
        batch.append(len(batch) + 1)

        sum_arg = sum_black + sum_red + sum_zero
        ball = random.randint(0, sum_arg - 1)

        if ball in select_six:
            money += bid * 6
            win += 1
        else:
            loose += 1
        if (win + loose) >= 100000:
            money = 0
    games = win + loose
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    show_arg()
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(
        win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(
        loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance, mode='lines', line=dict(color='purple', width=3)))
    fig.update_layout(title=dict(text=str(mode)))
    fig.update_xaxes(title_text='Количество сыгранных партий')
    fig.update_yaxes(title_text='Количество денежных средств')
    fig.show()


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# ========== Функции выбора и работы для режима игры ДЮЖИНА ==========


def dozen_select():
    global select_twelve_dozen
    print('\033[96m' + 'Вы выбрали режим "Дюжина". Введите далее порядковый номер дюжины, на которую вы ставите!' + '\033[0m')
    print('\033[90m' + 'Вводи ,пожалуйста, только числовое значение от 1 до 11, иначе всё сломается(' + '\033[0m')
    print(
        '\033[90m' + 'Кроме этого, не забывайте, что количества фишек сбрасываются до значений по умолчанию.' + '\033[0m')
    reset_sum()
    d = 0
    while d == 0:
        i = int(input())
        if i > 36 or i < 0:
            print(
                '\033[91m' + 'Введи значение не больше, чем число возможных порядковых номеров (11), а также не меньше нуля!' + '\033[0m')
        else:
            select_twelve_dozen = dozen_list[i]
            print('Вы выбрали следующую пару', str(select_twelve_dozen[0]) + ',' + str(select_twelve_dozen[1]) + ',' + str(select_twelve_dozen[2]) + ',' + str(select_twelve_dozen[3]) + ',' + str(select_twelve_dozen[4]) + ',' + str(select_twelve_dozen[5]) + ',' + str(select_twelve_dozen[5])+ ',' + str(select_twelve_dozen[6]) + ',' + str(select_twelve_dozen[7]) + ',' + str(select_twelve_dozen[8]) + ',' + str(select_twelve_dozen[9]) + ',' + str(select_twelve_dozen[10]) + ',' + str(select_twelve_dozen[11]))
            break


def dozen():
    win = 0
    loose = 0
    balance = []
    batch = []
    money = start_money
    while money > 0:
        bid = start_money * k

        if bid > money:
            bid = money

        money -= bid

        balance.append(money)
        batch.append(len(batch) + 1)

        sum_arg = sum_black + sum_red + sum_zero
        ball = random.randint(0, sum_arg - 1)

        if ball in select_twelve_dozen:
            money += bid * 3
            win += 1
        else:
            loose += 1
        if (win + loose) >= 100000:
            money = 0
    games = win + loose
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    show_arg()
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(
        win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(
        loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance, mode='lines', line=dict(color='purple', width=3)))
    fig.update_layout(title=dict(text=str(mode)))
    fig.update_xaxes(title_text='Количество сыгранных партий')
    fig.update_yaxes(title_text='Количество денежных средств')
    fig.show()


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# ========== Функции выбора и работы для режима игры КОЛОННА ========== #


def column_select():
    global select_twelve_column
    print('\033[96m' + 'Вы выбрали режим "Колонна". Введите далее порядковый номер колонны, на которую вы ставите!' + '\033[0m')
    print('\033[90m' + 'Вводи ,пожалуйста, только числовое значение от 1 до 3, иначе всё сломается(' + '\033[0m')
    print(
        '\033[90m' + 'Кроме этого, не забывайте, что количества фишек сбрасываются до значений по умолчанию.' + '\033[0m')
    reset_sum()
    d = 0
    while d == 0:
        i = int(input())
        if i > 36 or i < 0:
            print(
                '\033[91m' + 'Введи значение не больше, чем число возможных порядковых номеров (3), а также не меньше нуля!' + '\033[0m')
        else:
            select_twelve_column = column_list[i]
            print('Вы выбрали следующую пару', str(select_twelve_column[0]) + ',' + str(select_twelve_column[1]) + ',' + str(select_twelve_column[2]) + ',' + str(select_twelve_column[3]) + ',' + str(select_twelve_column[4]) + ',' + str(select_twelve_column[5]) + ',' + str(select_twelve_column[5])+ ',' + str(select_twelve_column[6]) + ',' + str(select_twelve_column[7]) + ',' + str(select_twelve_column[8]) + ',' + str(select_twelve_column[9]) + ',' + str(select_twelve_column[10]) + ',' + str(select_twelve_column[11]))
            break


def column():
    win = 0
    loose = 0
    balance = []
    batch = []
    money = start_money
    while money > 0:
        bid = start_money * k

        if bid > money:
            bid = money

        money -= bid

        balance.append(money)
        batch.append(len(batch) + 1)

        sum_arg = sum_black + sum_red + sum_zero
        ball = random.randint(0, sum_arg - 1)

        if ball in select_twelve_column:
            money += bid * 3
            win += 1
        else:
            loose += 1
        if (win + loose) >= 100000:
            money = 0
    games = win + loose
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    show_arg()
    print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(
        win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(
        loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance, mode='lines', line=dict(color='purple', width=3)))
    fig.update_layout(title=dict(text=str(mode)))
    fig.update_xaxes(title_text='Количество сыгранных партий')
    fig.update_yaxes(title_text='Количество денежных средств')
    fig.show()


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# ========== Главная функция по запуску расчёта игровой сессии ========== #
def run():
    if mode == 'На число':
        one_pos_select()
        one_pos()
    elif mode == 'Равные числа':
        half_pos_select()
        if mode_mode == 'Чёрное':
            half_pos_black()
        if mode_mode == 'Красное':
            half_pos_red()
        if mode_mode == 'Чётное':
            half_pos_even()
        if mode_mode == 'Нечётное':
            half_pos_odd()
        if mode_mode == 'Больше':
            half_pos_big()
        if mode_mode == 'Меньше':
            half_pos_small()
    elif mode == 'Сплит':
        split_select()
        split()
    elif mode == 'Стрит':
        street_select()
        street()
    elif mode == 'Угол':
        square_select()
        square()
    elif mode == 'Двойной Стрит':
        double_street_select()
        double_street()
    elif mode == 'Дюжина':
        dozen_select()
        dozen()
    elif mode == 'Колонна':
        column_select()
        column()


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

text_end()

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# ========== Ответ программы на команды ========== #
while f == 0:
    answer = input()
    if answer == 'help':
        help()
    elif answer == 'help_mode':
        help_mode()
    elif answer == 'show_board':
        show_board()
    elif answer == 'set_black':
        set_black()
    elif answer == 'set_red':
        set_red()
    elif answer == 'set_zero':
        set_zero()
    elif answer == 'set_k':
        set_k()
    elif answer == 'set_money':
        set_money()
    elif answer == 'set_mode':
        set_mode()
    elif answer == 'show_arg':
        show_arg()
    elif answer == 'positive':
        positive()
    elif answer == 'stop':
        stop()
        f = 1
    elif answer == 'reset':
        reset()
    elif answer == 'run':
        run()
    else:
        mistake()
