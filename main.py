import random
import plotly
import plotly.graph_objs as go

black = [1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 28, 30, 32, 34, 36]
white = [2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 20, 22, 24, 26, 29, 31, 33, 35]
mode_list=["На число", "Равные числа"]
mode_mode_list = ["Чёрное", "Красное", "Чётное", "Нечётное"]

start_money = 100000
k = 0.001
sum_black = 18
sum_red = 18
sum_zero = 1
mode='На число'

def show_arg():
    print(start_money, '\033[93m' + '<-начальная сумма денег' + '\033[0m')
    print(k, '\033[93m' + '<-начальный коэффицент ставок' + '\033[0m')
    print((start_money * k), '\033[93m' + '<-начальный коэффицент ставок' + '\033[0m')
    print(sum_black, '\033[93m' + '<-начальное количество чёрных ячеек' + '\033[0m')
    print(sum_red, '\033[93m' + '<-начальное количество белых ячеек' + '\033[0m')
    print(sum_zero, '\033[93m' + '<-начальное количество ячейки "зиро"' + '\033[0m')
    print(mode, '\033[93m' + '<-режим игры' + '\033[0m')
def text_end():
    print(' ')
    print('\033[96m' + '<Хотите, что-нибудь ЕЩЁ изменить?>' + '\033[0m')
    print('\033[92m' + '•Если нет, то погнали! Пиши команду "run" и смотри на результат!' + '\033[0m')
    print(' ')
    print('\033[92m' + '•Если да, то напиши команду "help" для вывода всех команд.' + '\033[0m')

show_arg()

text_end()

def help():
    print('show_arg', '\033[93m' + '<-Вывод списка начальных значений' + '\033[0m')
    print('set_black', '\033[93m' + '<-Задать количество чёрных фишек' + '\033[0m')
    print('set_red', '\033[93m' + '<-Задать количество белых фишек' + '\033[0m')
    print('set_zero', '\033[93m' + '<-Задать количество фишек "зиро"' + '\033[0m')
    print('set_k', '\033[93m' + '<-Задать коэффицент ставок' + '\033[0m')
    print('set_money', '\033[93m' + '<-Задать начальную сумму денег' + '\033[0m')
    print('help', '\033[93m' + '<-Вывод всех команд' + '\033[0m')
    print('help_mode', '\033[93m' + 'Вывод все возможных режимов игры и их подтипов' + '\033[0m')
def help_mode():
    print('show_arg', '\033[93m' + '<-Вывод списка начальных значений' + '\033[0m')
    print('set_black', '\033[93m' + '<-Задать количество чёрных фишек' + '\033[0m')
    print('set_red', '\033[93m' + '<-Задать количество белых фишек' + '\033[0m')
    print('set_zero', '\033[93m' + '<-Задать количество фишек "зиро"' + '\033[0m')
    print('set_k', '\033[93m' + '<-Задать коэффицент ставок' + '\033[0m')
    print('set_money', '\033[93m' + '<-Задать начальную сумму денег' + '\033[0m')
    print('help', '\033[93m' + '<-Вывод всех команд' + '\033[0m')
    print('help_mode', '\033[93m' + 'Вывод все возможных режимов игры и их подтипов' + '\033[0m')

def set_black():
    print('\033[90m' + 'Вводи ,пожалуйста, только числовое значение, иначе всё сломается(')
    i = int(input())
    if i > 37 or i <= 0:
        print('\033[91m''Введи значение не больше, чем число возможных ячеек (30), а также не меньше нуля!' + '\033[0m')
    else:
        sum_black = i
        print('Начальное количество чёрных ячеек изменено на :', '\033[93m' + str(sum_black) + '\033[0m')

    text_end()
def set_red():
    print('\033[90m' + 'Вводи ,пожалуйста, только числовое значение, иначе всё сломается(' + '\033[0m')
    i = 0
    i = int(input())
    if i > 37 or i <= 0:
        print(
            '\033[91m' + 'Введи значение не больше, чем число возможных ячеек (30), а также не меньеш нуля!' + '\033[0m')
    else:
        sum_red = i
        print('Начальное количество красных ячеек изменено на :', '\033[93m' + str(sum_red) + '\033[0m')
    text_end()
def set_zero():
    print('\033[90m' + 'Вводи ,пожалуйста, только числовое значение, иначе всё сломается(' + '\033[0m')
    i = 0
    i = int(input())
    if i < 0 or i > 1:
        print(
            '\033[91m' + 'Введи значение не больше, чем число возможных фишек (1), а также не меньше нуля!' + '\033[0m')
    else:
        sum_zero = i
        print('Начальное количество "зиро" ячеек изменено на :', '\033[93m' + str(sum_zero) + '\033[0m')
    text_end()
def set_k():
    print('\033[90m' + 'Вводи ,пожалуйста, только числовое значение от 0 до 1, иначе всё сломается(' + '\033[0m')
    d = 0
    while d == 0:
        i = 0
        i = float(input())
        if i < 0 or i >= 1:
            print(
                '\033[91m' + 'Введи значение не больше, чем число возможных фишек (30), а также не меньше нуля!' + '\033[0m')
            d = 0
        else:
            k = i
            d += 1
            print('Начальный коэффицент ставок изменён на:', '\033[93m' + str(k) + '\033[0m')
    text_end()
def set_money():
    print('\033[90m' + 'Вводи ,пожалуйста, только числовое значение от 0 до 1, иначе всё сломается(' + '\033[0m')
    i = int(input())
    if i < 0:
        print('\033[91m' + 'Введи значение не меньше нуля!' + '\033[0m')
    else:
        start_money = i
        print('Начальное количество денег изменено на:', '\033[93m' + str(start_money) + '\033[0m')
    text_end()
def set_mode():
    print('\033[90m' + 'Все возможные режимы игры и их подтипы можно узнать по команде "help_mode"' + '\033[0m')
    i = input()
    if i not in mode_list:
        print('\033[91m' + 'Такого режима игры нет( Введите существующий!' + '\033[0m')
    else:
        mode = i
        print('Режим игры изменён на :', '\033[93m' + str(mode) + '\033[0m')
    text_end()


def positive():
    print('\033[91m' + 'Оставайся всегда позитивным!' + '\033[0m')
def stop():
    print('\033[91m' + 'Буду рад предсказать игру ещё раз! До встречи!' + '\033[0m')
    с = 0
def mistake():
    print('\033[91m' + 'Такой команды нет(' + '\033[0m')
    print('\033[92m' + 'Напиши команду "help_list" для вывода всех команд, если ты вдруг их забыл' + '\033[0m')

def run():
    if mode == 'На число':
        print('\033[96m' +  'Вы выбрали режим "Моё число". Введите далее число, на которое вы ставите!' + '\033[0m')
        print('\033[90m' + 'Вводи ,пожалуйста, только числовое значение от 0 до 36, иначе всё сломается(' + '\033[0m')
        i = int(input())
        if i > 36 or i < 0:
            print('\033[91m' + 'Введи значение не больше, чем число возможных ячеек (38), а также не меньше нуля!' + '\033[0m')
        else:
            select = i
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
            ball = random.randint(0, sum_arg-1)

            if ball == select:
                money += bid * 36
                win += 1
            else:
                loose += 1
            if (win+loose) >= 100000:
                money = 0
        games = win + loose
        print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
        print(start_money, '\033[93m' + '<-начальная сумма денег' + '\033[0m')
        print(k, '\033[93m' + '<-начальный коэффицент ставок' + '\033[0m')
        print((start_money * k), '\033[93m' + '<-начальный коэффицент ставок' + '\033[0m')
        print(sum_black, '\033[93m' + '<-начальное количество чёрных ячеек' + '\033[0m')
        print(sum_red, '\033[93m' + '<-начальное количество белых ячеек' + '\033[0m')
        print(sum_zero, '\033[93m' + '<-начальное количество ячейки "зиро"' + '\033[0m')
        print(mode, '\033[93m' + '<-режим игры' + '\033[0m')
        print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
        print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(win / games * 100) + "%). "+ '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(loose / games * 100) + "%). "+ '\033[0m')
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=batch, y=balance))
        fig.show()
        c = 0
    if mode == 'Равные числа':
        print('\033[96m' +  'Уточните тип игры "Равные числа"!' + '\033[0m')
        i = 0
        while i == 0:
            mode_mode = input()
            if mode_mode in mode_mode_list:
                print('Режим игры изменён на: ', mode+" "+mode_mode)
                i += 1
            elif mode_mode != 'help_mode':
                print('\033[91m' + 'Такого подтипа режима игры "Равные числа "нет(' + '\033[0m')
                print('\033[93m' + 'Все возможные режимы игры и их подтипы можно узнать по команде "help_mode"' + '\033[0m')
            else:
                help_mode()
        if mode_mode == 'Чёрное':
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
                if (win+loose) >= 100000:
                    money = 0
            games = win + loose
            print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
            print(start_money, '\033[93m' + '<-начальная сумма денег' + '\033[0m')
            print(k, '\033[93m' + '<-начальный коэффицент ставок' + '\033[0m')
            print((start_money * k), '\033[93m' + '<-начальный коэффицент ставок' + '\033[0m')
            print(sum_black, '\033[93m' + '<-начальное количество чёрных ячеек' + '\033[0m')
            print(sum_red, '\033[93m' + '<-начальное количество белых ячеек' + '\033[0m')
            print(sum_zero, '\033[93m' + '<-начальное количество ячейки "зиро"' + '\033[0m')
            print(mode, '\033[93m' + '<-режим игры' + '\033[0m')
            print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
            print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(win / games * 100) + "%). "+ '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(loose / games * 100) + "%). "+ '\033[0m')
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=batch, y=balance))
            fig.show()
            c = 0
        if mode_mode == 'Красное':
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

                range_red = sum_red + 1
                if ball in white:
                    money += bid * 2
                    win += 1
                else:
                    loose += 1
                if (win + loose) >= 100000:
                    money = 0
            games = win + loose
            print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
            print(start_money, '\033[93m' + '<-начальная сумма денег' + '\033[0m')
            print(k, '\033[93m' + '<-начальный коэффицент ставок' + '\033[0m')
            print((start_money * k), '\033[93m' + '<-начальный коэффицент ставок' + '\033[0m')
            print(sum_black, '\033[93m' + '<-начальное количество чёрных ячеек' + '\033[0m')
            print(sum_red, '\033[93m' + '<-начальное количество белых ячеек' + '\033[0m')
            print(sum_zero, '\033[93m' + '<-начальное количество ячейки "зиро"' + '\033[0m')
            print(mode, '\033[93m' + '<-режим игры' + '\033[0m')
            print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
            print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(
                win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(
                loose / games * 100) + "%). " + '\033[0m')
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=batch, y=balance))
            fig.show()
            c = 0
        if mode_mode == 'Чётное':
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

                if (ball%2) == 0:
                    money += bid * 2
                    win += 1
                else:
                    loose += 1
                if (win + loose) >= 100000:
                    money = 0
            games = win + loose
            print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
            print(start_money, '\033[93m' + '<-начальная сумма денег' + '\033[0m')
            print(k, '\033[93m' + '<-начальный коэффицент ставок' + '\033[0m')
            print((start_money * k), '\033[93m' + '<-начальный коэффицент ставок' + '\033[0m')
            print(sum_black, '\033[93m' + '<-начальное количество чёрных ячеек' + '\033[0m')
            print(sum_red, '\033[93m' + '<-начальное количество белых ячеек' + '\033[0m')
            print(sum_zero, '\033[93m' + '<-начальное количество ячейки "зиро"' + '\033[0m')
            print(mode, '\033[93m' + '<-режим игры' + '\033[0m')
            print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
            print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(
                win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(
                loose / games * 100) + "%). " + '\033[0m')
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=batch, y=balance))
            fig.show()
            c = 0
        if mode_mode == 'Нечётное':
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

                if (ball%2) != 0:
                    money += bid * 2
                    win += 1
                else:
                    loose += 1
                if (win + loose) >= 100000:
                    money = 0
            games = win + loose
            print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
            print(start_money, '\033[93m' + '<-начальная сумма денег' + '\033[0m')
            print(k, '\033[93m' + '<-начальный коэффицент ставок' + '\033[0m')
            print((start_money * k), '\033[93m' + '<-начальный коэффицент ставок' + '\033[0m')
            print(sum_black, '\033[93m' + '<-начальное количество чёрных ячеек' + '\033[0m')
            print(sum_red, '\033[93m' + '<-начальное количество белых ячеек' + '\033[0m')
            print(sum_zero, '\033[93m' + '<-начальное количество ячейки "зиро"' + '\033[0m')
            print(mode, '\033[93m' + '<-режим игры' + '\033[0m')
            print('ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
            print('\033[92m' + "Выиграно ставок: " + str(win) + " (" + str(
                win / games * 100) + "%). " + '\033[0m' + '\033[91m' + " Проиграно ставок: " + str(loose) + " (" + str(
                loose / games * 100) + "%). " + '\033[0m')
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=batch, y=balance))
            fig.show()
            c = 0

c = 0
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
    elif answer == 'run':
        run()
    else:
        mistake()

