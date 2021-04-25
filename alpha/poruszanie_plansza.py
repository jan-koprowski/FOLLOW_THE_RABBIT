"""
RUCHY
1 - góra
2 - góra-prawo
3 - prawo
4 - dół-prawo
5 - dół
6 - dól-lewo
7 - lewo
8 - góra-lewo
9--cel 
plansza wygenerowana na liczbach zeby lepiej wygladala 
"""
# -*- coding: utf-8 -*-

def board(Table):
    # -*- coding: utf-8 -*-
    my_db = []
    # pole n(x) na m(y)
    n = 5
    m = 5
    plansza = [[0 for col in range(n)] for row in range(m)]

    #pionek
    x = 3
    y = 3
    plansza[y][x] = 1

    for ruch in Table:
        if ruch == 1: #góra
            if y > 0:
                plansza[y][x] = 0
                y = y - 1
                plansza[y][x] = 1

            elif y <= 0:
                plansza[y][x] = 0
                y = y+1
                plansza[y][x] = 1
            print(f'{x}{y}')
            my_db.append(f'{x}{y}')

        if ruch == 5: #dol
            if y < m-1:
                plansza[y][x] = 0
                y = y + 1
                plansza[y][x] = 1
            elif y >= m-1:
                plansza[y][x] = 0
                y = y - 1
                plansza[y][x] = 1
            print(f'{x}{y}')
            my_db.append(f'{x}{y}')

        if ruch == 3: #prawo
            if x < n-1:
                plansza[y][x] = 0
                x = x + 1
                plansza[y][x] = 1
            elif x >= n-1:
                plansza[y][x] = 0
                x = x - 1
                plansza[y][x] = 1
            print(f'{x}{y}')
            my_db.append(f'{x}{y}')

        if ruch == 7: #lewo
            if x > 0:
                plansza[y][x] = 0
                x = x - 1
                plansza[y][x] = 1
            elif x <= 0:
                plansza[y][x] = 0
                x = x+1
                plansza[y][x] = 1
            print(f'{x}{y}')
            my_db.append(f'{x}{y}')


        if ruch == 2: #gora-prawo
            if y > 0 and x < n-1:
                plansza[y][x] = 0
                y = y - 1
                x = x + 1
                plansza[y][x] = 1
            elif y <= 0 and x >= n-1: #odbicie
                plansza[y][x] = 0
                y = y + 1
                x = x - 1
                plansza[y][x] = 1
            elif x >= n-1: #jesli nie moge w prawo to tylko do gory
                plansza[y][x] = 0
                y = y - 1
                plansza[y][x] = 1
            elif y <= 0: #jesli nie moge do gory to tylko w prawo
                plansza[y][x] = 0
                x = x + 1
                plansza[y][x] = 1
            print(f'{x}{y}')
            my_db.append(f'{x}{y}')


        if ruch == 8: #gora-lewo
            if y > 0 and x > 0:
                plansza[y][x] = 0
                y = y - 1
                x = x - 1
                plansza[y][x] = 1
            elif y <= 0 and x <= 0:  # odbicie
                plansza[y][x] = 0
                y = y + 1
                x = x + 1
                plansza[y][x] = 1
            elif x <= 0:  # jesli nie moge w lewo to tylko do gory
                plansza[y][x] = 0
                y = y - 1
                plansza[y][x] = 1
            elif y <= 0:  # jesli nie moge do gory to tylko w lewo
                plansza[y][x] = 0
                x = x - 1
                plansza[y][x] = 1
            print(f'{x}{y}')
            my_db.append(f'{x}{y}')

        if ruch == 4: #dol-prawo
            if y < m-1 and x < n - 1:
                plansza[y][x] = 0
                y = y + 1
                x = x + 1
                plansza[y][x] = 1
            elif y >= m-1 and x >= n - 1:  # odbicie
                plansza[y][x] = 0
                y = y - 1
                x = x - 1
                plansza[y][x] = 1
            elif x >= n - 1:  # jesli nie moge w prawo to tylko w dol
                plansza[y][x] = 0
                y = y + 1
                plansza[y][x] = 1
            elif y >= m-1:  # jesli nie moge w dol to tylko w prawo
                plansza[y][x] = 0
                x = x + 1
                plansza[y][x] = 1
            print(f'{x}{y}')
            my_db.append(f'{x}{y}')

        if ruch == 6: #dol-lewo
            if y < m-1 and x > 0:
                plansza[y][x] = 0
                y = y + 1
                x = x - 1
                plansza[y][x] = 1
            elif y >= m-1 and x <= 0:  # odbicie
                plansza[y][x] = 0
                y = y - 1
                x = x + 1
                plansza[y][x] = 1
            elif x <= 0:  # jesli nie moge w lewo to tylko w dol
                plansza[y][x] = 0
                y = y + 1
                plansza[y][x] = 1
            elif y >= m-1:  # jesli nie moge w dol to tylko w lewo
                plansza[y][x] = 0
                x = x - 1
                plansza[y][x] = 1
            print(f'{x}{y}')
            my_db.append(f'{x}{y}')
    return my_db

