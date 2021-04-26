# -*- coding: utf-8 -*-

import sys
from db import add_to_db
from poruszanie_plansza import board


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