import random
import os

ELEMENTS = 100


new_table = [] # do tego maja byc odczytane dane z pliku przesłanego do alphy
direction = ["A","B", "C","D"]
for x in range(ELEMENTS):
    new_table.append(random.choice(direction))
# print(new_table)


step_board = [] # Tabilca na dane

# Początkowy punkt startu
x = 25

for element in new_table:
    step_board.append(x)
    if element == "A": #Rusz sie do gory
        if (x == 1 or x == 2 or x == 3 or x == 4 or x == 5 or x == 6 or x == 7):
            x+=7
        else:
            x -= 7
    if element == "B": #Rusz sie w prawo
        if (x == 28 or x == 21 or x == 14 or x == 7 or x == 35 or x == 42 or x == 49):
            x-=1
        else:
            x += 1
    if element == "C": #Rusz sie do dolu
        if (x == 43 or x == 44 or x == 45 or x == 46 or x == 47 or x == 48 or x == 49):
            x-=7
        else:
            x += 7
    if element == "D": #Rusz sie w lewo
        if (x == 1 or x == 8 or x == 15 or x == 22 or x == 29 or x == 35 or x == 43):
            x+=1
        else:
            x -= 1


# print(step_board)
# print(f"Długosc tabeli a = {len(new_table)}")
# print(f"Długosc tabeli b = {len(step_board)}")


def save_to_file():
    for element in step_board:
        cmd = 'echo \"' + str(element) + ' \">> out_test.txt'
        os.system(cmd)

def calculate_combinations():
    numbers_of_1 = 0
    numbers_of_7 = 0
    numbers_of_43 = 0
    numbers_of_49 = 0
    for element in step_board:
        if element == 1:
            numbers_of_1 += 1
            # print(f"1 uzyskaliśmy jak {step_board[element]} tablicy")
        if element == 7:
            numbers_of_7 += 1
            # print(f"7 uzyskaliśmy jak {step_board[element]} tablicy")
        if element == 43:
            numbers_of_43 += 1
            # print(f"43 uzyskaliśmy jak {step_board[element]} tablicy")
        if element == 49:
            numbers_of_49 += 1
            # print(f"49 uzyskaliśmy jak {step_board[element]} tablicy")
    print('Liczba ogólnie uzyskanych elementów:')
    print(f'Dla 1 {numbers_of_1/ELEMENTS*100}')
    print(f'Dla 7 {numbers_of_7/ELEMENTS*100}')
    print(f'Dla 43 {numbers_of_43/ELEMENTS*100}')
    print(f'Dla 49 {numbers_of_49/ELEMENTS*100}')

calculate_combinations()