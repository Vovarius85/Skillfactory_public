# При реализации итогового задания по второму блоку был выбран гибридный вариант между моими идеями и кодом из вебинара
# по разбору итогового задания. Из вебинара была взята функция по вводу в игровое поле крестиков и ноликов, он
# был значительно короче, читаемее и красивее, чем у меня. Так же из вебинара забрал идею со счетиком ходов: четный ход -
# ходит игрок 1, не четный - ходит игрок 2. Остальное, это мои идеи, появившиеся по итогам прохождения 2-го блока.

def priority_players():  # Функция для определения очередности ходов. Игра "Камень, ножницы, бумага".
        while True:
            var_player_1 = input("Введите в английской раскладке: s - камень, v - ножницы, p - бумага - ")
            if var_player_1 in ['s', 'v', 'p']:
                print()
                break

            else:
                print("Вы нажали ошибочный вариант. Попробуйте снова")

        while True:
            var_player_2 = input("Введите в английской раскладке: s - камень, v - ножницы, p - бумага - ")
            if var_player_2 in ['s', 'v', 'p']:
                print()
                break

            else:
                print("Вы нажали ошибочный вариант. Попробуйте снова")

        return var_player_1, var_player_2

def print_field_of_game():   # Функция отображения игрового поля.
    for x in range(N):
        for y in range(M):
            print(field_of_game[y][x], end="  ")
        print()

def ask():  # Функция ввода крестиков-ноликов в игровое поле
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        y, x = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        y, x = int(y), int(x)

        if 0 > x or x > 3 or 0 > y or y > 3:
            print(" Координаты вне диапазона! ")
            continue

        if field_of_game[y][x] != ' ':
            print(" Клетка занята! ")
            continue

        return y, x

def var_win():  # Функция определения победных комбинаций
    if (field_of_game[1].count('X') == 3 or field_of_game[2].count('X') == 3 or field_of_game[3].count('X') == 3 or
            (field_of_game[1][1] == 'X' and field_of_game[2][2] == 'X' and field_of_game[3][3] == 'X') or
            (field_of_game[1][3] == 'X' and field_of_game[2][2] == 'X' and field_of_game[3][1] == 'X')):
        print(f"Победил игрок {list_of_players[0]}")

        return True

    if (field_of_game[1].count('O') == 3 or field_of_game[2].count('O') == 3 or field_of_game[3].count('O') == 3 or
            (field_of_game[1][1] == 'O' and field_of_game[2][2] == 'O' and field_of_game[3][3] == 'O') or
            (field_of_game[1][3] == 'O' and field_of_game[2][2] == 'O' and field_of_game[3][1] == 'O')):
        print(f"Победил игрок {list_of_players[1]}")

        return True

    return False

print('Игра крестики-нолики')
player_1 = input("Введите имя игрока - ")
player_2 = input("Введите имя игрока - ")
list_of_players = []
N = 4
M = 4
field_of_game = [
    [' ', '1', '2', '3'],
    ['1', ' ', ' ', ' '],
    ['2', ' ', ' ', ' '],
    ['3', ' ', ' ', ' ']
]
print("Определим очередность хода игроков игрой 'Камень, ножницы, бумага'")
while True:
    var_player_1, var_player_2 = priority_players()
    if var_player_1 == var_player_2:
        print("Ничья. Попробуйте снова")
        continue

    elif ((var_player_1 == 's' and var_player_2 == 'v') or (var_player_1 == 'v' and var_player_2 == 'p') or
          (var_player_1 == 'p' and var_player_2 == 's')):
        list_of_players = [player_1, player_2]
        print(f"Победил игрок {list_of_players[0]}", f"Первым ходит: {list_of_players[0]}",
              f"Вторым ходит: {list_of_players[1]}", sep='\n')
        break

    else:
        list_of_players = [player_2, player_1]
        print(f"Победил игрок {list_of_players[0]}", f"Первым ходит: {list_of_players[0]}",
              f"Вторым ходит: {list_of_players[1]}", sep='\n')
        break

count = 0
while True:
    count += 1
    print_field_of_game()
    if count % 2 == 1:
        print(f" Ходит {list_of_players[0]}, введите цифры через пробел")
    else:
        print(f" Ходит {list_of_players[1]}, введите цифры через пробел")

    x, y = ask()

    if count % 2 == 1:
        field_of_game[x][y] = "X"
    else:
        field_of_game[x][y] = "0"

    if var_win():
        break

    if count == 9:
        print(" Ничья!")
        break
