# -*- coding: utf-8 -*-

import sys
from db import add_to_db


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
            
            # print(f'{x}{y}')
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
            # print(f'{x}{y}')
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
            # print(f'{x}{y}')
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
            # print(f'{x}{y}')
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
            # print(f'{x}{y}')
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
            # print(f'{x}{y}')
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
            # print(f'{x}{y}')
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
            # print(f'{x}{y}')
            my_db.append(f'{x}{y}')
    return my_db




fake_db = []

def main(files):
    for f in files:
        f = open('files/' +f, "r")
        data = f.readlines()
        for element in data:
            # print(element.rstrip("\n"))
            if len(element) > 6:
                fake_db.append(element.rstrip("\n"))
            else:
                fake_db.append(int(element.rstrip("\n")))
        
        # print(fake_db)
        # print(board(fake_db[1:]))
        add_to_db(fake_db[0], board(fake_db[1:]))



if __name__ == "__main__":
    files = sys.argv[1:]
    main(files)