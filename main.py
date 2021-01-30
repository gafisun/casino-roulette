import random
import plotly
import plotly.graph_objs as go
import shutil
import requests
from PIL import Image

a = 0
c = 0
red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)
black = (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)
split_list = ([0, 1], [0, 2], [0, 3], [1, 0], [1, 2], [1, 4], [2, 0], [2, 1], [2, 3], [2, 5], [3, 0], [3, 2], [3, 6], [4, 1], [4, 5], [4, 7], [5, 4], [5, 2], [5, 6], [5, 8], [7, 4], [7, 8], [7, 10], [8, 7], [8, 5], [8, 9], [8, 11], [9, 8], [9, 6], [9, 12], [10, 13], [10, 7], [10, 11], [11, 10], [11, 8], [11, 12], [11, 14], [12, 11], [12, 9], [12, 15], [13, 16], [13, 10], [13, 14], [14, 13], [14, 11], [14, 15], [14, 17], [15, 18], [15, 14], [15, 12], [16, 19], [16, 17], [16, 13], [17, 16], [17, 14], [17, 18], [17, 20], [18, 21], [18, 17], [18, 15], [19, 22], [19, 20], [19, 16], [20, 19], [20, 17], [20, 21], [20, 23], [21, 24], [21, 20], [21, 18], [22, 25], [22, 23], [22, 19], [23, 26], [23, 22], [23, 20], [23, 24], [24, 27], [24, 23], [24, 21], [25, 28], [25, 26], [25, 22], [26, 29], [26, 25], [26, 23], [26, 27], [27, 30], [27, 26], [27, 24], [28, 31], [28, 29], [28, 25],  [29, 32], [29, 28], [29, 26], [29, 30], [30, 33], [30, 29], [30, 27], [31, 34], [31, 32], [31, 28], [32, 35], [32, 31], [32, 29], [32, 33], [33, 36], [33, 32], [33, 30], [34, 35], [34, 31], [35, 34], [35, 32], [35, 36], [36, 35], [36, 33])
street_list = {1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9], 4:[10, 11, 12], 5:[13, 14, 15], 6:[16, 17, 18], 7:[19, 20, 21], 8:[22, 23, 24], 9:[25, 26, 27], 10:[28, 29, 30], 11:[31, 32, 33], 12:[34, 35, 36]}
kare_list = ()
double_street_list = ()
mode_list = ("На число", "Равные числа", "Сплит", "Стрит", "Каре", "Двойной Стрит", "Дюжина", "")
mode_mode_list = ("Чёрное", "Красное", "Чётное", "Нечётное", "Меньше", "Больше")
random_picture = random.random()

start_money = 100000
k = 0.001
sum_black = 18
sum_red = 18
sum_zero = 1
mode = 'Сплит'
mode_mode = ''
select_one = -1
select_two = []


def show_arg():
    print(start_money, '\033[93m' + '<-начальная сумма денег' + '\033[0m')
    print(k, '\033[93m' + '<-начальный коэффицент ставок' + '\033[0m')
    print((start_money * k), '\033[93m' + '<-начальная сумма ставок' + '\033[0m')
    print(sum_black, '\033[93m' + '<-начальное количество чёрных ячеек' + '\033[0m')
    print(sum_red, '\033[93m' + '<-начальное количество белых ячеек' + '\033[0m')
    print(sum_zero, '\033[93m' + '<-начальное количество ячейки "зиро"' + '\033[0m')
    print(mode, '\033[93m' + '<-режим игры' + '\033[0m')
    if len(mode_mode) != 0 and mode == 'Равные числа':
        print(mode_mode, '\033[93m' + '<-Тип режима игры "Равные числа"' + '\033[0m')
    elif len(mode_mode) == 0 and mode == 'Равные числа':
        print('Тип режима игры "Равные числа" ','\033[91m' + 'не выбран!'+ '\033[0m')
    if select_one <=37 and select_one > -1:
        print(select_one, '\033[93m' + '<-Выбранное число для режима игры "На число"' + '\033[0m')
def text_end():
    print(' ')
    print('\033[96m' + '<Хотите, что-нибудь ЕЩЁ изменить?>' + '\033[0m')
    print('\033[92m' + '•Если нет, то погнали! Пиши команду "run" и смотри на результат!' + '\033[0m')
    print(' ')
    print('\033[92m' + '•Если да, то напиши команду "help" для вывода всех команд.' + '\033[0m')


show_arg()
# Функции закачки из сети и вывода изображения игральной доски
my_url = 'https://static.vecteezy.com/system/resources/previews/000/155/653/original/green-roulette-table-vector.jpg'
response = requests.get(my_url, stream=True)
with open(str(random_picture)+'.png', 'wb') as file:
    shutil.copyfileobj(response.raw, file)
del response
img = Image.open(str(random_picture)+'.png')
img.show()

# Функции по выводу справочной информации о всевозможных командах и типах игры
def help():
    print('show_arg', '\033[93m' + '<-Вывод списка начальных значений' + '\033[0m')
    print('set_black', '\033[93m' + '<-Задать количество чёрных фишек' + '\033[0m')
    print('set_red', '\033[93m' + '<-Задать количество белых фишек' + '\033[0m')
    print('set_zero', '\033[93m' + '<-Задать количество фишек "зиро"' + '\033[0m')
    print('set_k', '\033[93m' + '<-Задать коэффицент ставок' + '\033[0m')
    print('set_money', '\033[93m' + '<-Задать начальную сумму денег' + '\033[0m')
    print('set_mode', '\033[93m' + '<-Задать режим игры' + '\033[0m')
    print('stop', '\033[93m' + '<-Выйти из игры' + '\033[0m')
    print('help', '\033[93m' + '<-Вывод всех команд' + '\033[0m')
    print('help_mode', '\033[93m' + 'Вывод все возможных режимов игры и их подтипов' + '\033[0m')
def help_mode():
    print('На число', '\033[93m' + '<-Ставка на одно выбранное вами число. В случае победы возвращается ставка * 36.' + '\033[0m')
    print('Равные числа', '\033[93m' + '<-Ставка на половину ячеек по определённому признаку (не включая "зиро"). В случае победы возвращается ставка * 2.' + '\033[0m')
    print('\033[94m' + '             •Чёрное' + '\033[0m', '\033[93m' + '<-Ставка на ячейки чёрного цвета.' + '\033[0m')
    print('\033[94m' + '             •Красное'+ '\033[0m', '\033[93m' + '<-Ставка на ячейки красного цвета.' + '\033[0m')
    print('\033[94m' + '             •Чётное' + '\033[0m', '\033[93m' + '<-Ставка на ячейки с чётным номером.' + '\033[0m')
    print('\033[94m' + '             •Нечётное' + '\033[0m', '\033[93m' + '<-Ставка на ячейки с нечётном номером.' + '\033[0m')
    print('\033[94m' + '             •Меньше' + '\033[0m', '\033[93m' + '<-Ставка на ячейки с 1 по 17 (включительно).' + '\033[0m')
    print('\033[94m' + '             •Больше' + '\033[0m', '\033[93m' + '<-Ставка на ячейки с 18 по 36 (включительно).' + '\033[0m')

# Функции настройки начальных значений
def set_black():
    global sum_black
    print('\033[90m' + 'Вводи ,пожалуйста, только числовое значение, иначе всё сломается('+ '\033[0m')
    d = 0
    while d == 0:
        i = int(input())
        if i > 37 or i <= 0:
            print('\033[91m' + 'Введи значение не больше, чем число возможных ячеек (36), а также не меньше нуля!' + '\033[0m')
        else:
            sum_black = i
            print('Начальное количество чёрных ячеек изменено на :', '\033[93m' + str(sum_black) + '\033[0m')
            d += 1

        text_end()
def set_red():
    global sum_red
    print('\033[90m' + 'Вводи ,пожалуйста, только числовое значение, иначе всё сломается(' + '\033[0m')
    d = 0
    while d == 0:
        i = int(input())
        if i > 37 or i <= 0:
            print('\033[91m' + 'Введи значение не больше, чем число возможных ячеек (36), а также не меньше нуля!' + '\033[0m')
        else:
            sum_red = i
            print('Начальное количество красных ячеек изменено на :', '\033[93m' + str(sum_red) + '\033[0m')
            d += 1
    text_end()
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

# Функции необходимы для ошибок в работе программы
def positive():
    print('\033[91m' + 'Оставайся всегда позитивным!' + '\033[0m')
def stop():
    global c
    print('\033[91m' + 'Буду рад предсказать игру ещё раз! До встречи!' + '\033[0m')
def mistake():
    print('\033[91m' + 'Такой команды нет(' + '\033[0m')
    print('\033[92m' + 'Напиши команду "help_list" для вывода всех команд, если ты вдруг их забыл.' + '\033[0m')
    print('\033[92m' + 'Для выхода из игры, напиши команду "stop".' + '\033[0m')

# Функции выбора и работы для режима игры НА ЧИСЛО
def one_pos_select():
    global select_one
    print('\033[96m' + 'Вы выбрали режим "Моё число". Введите далее число, на которое вы ставите!' + '\033[0m')
    print('\033[90m' + 'Вводи ,пожалуйста, только числовое значение от 0 до 36, иначе всё сломается(' + '\033[0m')
    d = 0
    while d == 0:
        i = int(input())
        if i > 36 or i < 0:
            print('\033[91m' + 'Введи значение не больше, чем число возможных ячеек (38), а также не меньше нуля!' + '\033[0m')
        else:
            select_one = i
            d += 1
    win = 0
    loose = 0
    games = 0
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
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance, name=str(mode)))
    fig.show()
    c = 0

# Функции выбора и работа для каждого типа режима игры РАВНЫЕ ЧИСЛА
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
def half_pos_black():
    win = 0
    loose = 0
    games = 0
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
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance))
    fig.show()
def half_pos_red():
    win = 0
    loose = 0
    games = 0
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
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance))
    fig.show()
    c = 0
def half_pos_even():
    win = 0
    loose = 0
    games = 0
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
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance))
    fig.show()
    c = 0
def half_pos_odd():
    win = 0
    loose = 0
    games = 0
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
    fig.add_trace(go.Scatter(x=batch, y=balance))
    fig.show()
    c = 0
def half_pos_big():
    win = 0
    loose = 0
    games = 0
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

        if ball >= 18 :
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
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance))
    fig.show()
def half_pos_small():
    win = 0
    loose = 0
    games = 0
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
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance))
    fig.show()
# Функция выбора и работы для режима игры СПЛИТ
def split_select():
    global select_two
    print('\033[96m' + 'Вы выбрали режим "Сплит". Введите далее 2 числа, нарисованные рядом друг с другом на поле, на которое вы ставите!' + '\033[0m')
    print('\033[90m' + 'Вводи ,пожалуйста, только числовые значения от 0 до 36, иначе всё сломается(' + '\033[0m')
    d = 0
    while d == 0:
        select_two = []
        a, b= map(int, input().split())
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
    games = 0
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
    print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(loose / games * 100) + "%). " + '\033[0m')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=batch, y=balance))
    fig.show()
# Функции выбора и работы для режима игры СТРИТ
#def street_select():
#def street():
# Функции выбора и работы для режима игры КАРЕ
#def kare_select():
#def kare():

# Функции выбора и работы для режима игры ДВОЙНОЙ СТРИТ
#def double_street_select():
#def double_street():
# Функции выбора и работы для режима игры ДЮЖИНА
#def dozen_select():
#def dozen():

# Главная функция по запуску расчёта игры
def run():
    if mode == 'На число':
        one_pos_select()
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
        street_select ()
        street()
    elif mode == 'Каре':
        kare_select ()
        kare ()
    elif mode == 'Двойной Стрит':
        double_street_select()
        double_street()
    elif mode == 'Дюжина':
        dozen_select()
        dozen()


# Ответ программы на команды
while c == 0:
    answer = input()
    if answer == 'help':
        help()
    elif answer == 'help_mode':
        help_mode()
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
        c = 1
    elif answer == 'run':
        run()
    else:
        mistake()
