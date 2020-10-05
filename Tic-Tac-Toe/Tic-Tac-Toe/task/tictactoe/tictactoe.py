field = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]
move_counter = 1


def print_field():
    print('-' * 9)
    print('|',field[0][0],field[0][1],field[0][2],'|')
    print('|',field[1][0],field[1][1],field[1][2],'|')
    print('|',field[2][0],field[2][1],field[2][2],'|')
    print('-' * 9)


def result():
    global end_game
    x_wins = 0
    o_wins = 0
    count_X_column = 0
    count_Y_column = 0
    rows = 3
    columns = 3
    for row in range(rows):
        for column in range(columns):
            if field[row][column] == 'X':
                count_X_column += 1
            if field[row][column] == 'O':
                count_Y_column += 1
        if count_X_column == 3:
            x_wins += 1
        if count_Y_column == 3:
            o_wins += 1
        count_X_column = 0
        count_Y_column = 0

    count_X_row = 0
    count_Y_row = 0
    for column in range(columns):
        for row in range(rows):
            if field[row][column] == 'X':
                count_X_row += 1
            if field[row][column] == 'O':
                count_Y_row += 1
        if count_X_row == 3:
            x_wins += 1
        if count_Y_row == 3:
            o_wins += 1
        count_X_row = 0
        count_Y_row = 0
    if field[0][0] == 'X' and field[1][1] == 'X' and field[2][2] == 'X':
        x_wins += 1
    if field[2][0] == 'X' and field[1][1] == 'X' and field[0][2] == 'X':
        x_wins += 1
    if field[0][0] == 'O' and field[1][1] == 'O' and field[2][2] == 'O':
        o_wins += 1
    if field[2][0] == 'O' and field[1][1] == 'O' and field[0][2] == 'O':
        o_wins += 1

    if x_wins == 1:
        print('X wins')
        end_game = True
    if o_wins == 1:
        print('O wins')
        end_game = True
    if x_wins == 0 and o_wins == 0 and sum(x.count(' ') for x in field) == 0:
        print('Draw')
        end_game = True
    if x_wins == 0 and o_wins == 0 and sum(x.count(' ') for x in field) > 0:
        print('Game not finished')


print_field()
end_game = False

while end_game is False:

    coordinates = input('Choose coordinates: ')

    while coordinates[0].isnumeric() is False or coordinates[-1].isnumeric() is False:
        print('You should enter numbers!')
        coordinates = input()

    while int(coordinates[0]) < 1 or int(coordinates[0]) > 3 or int(coordinates[-1]) < 1 or int(coordinates[-1]) > 3:
        print('Coordinates should be from 1 to 3!')
        coordinates = input()
        chosen_field = field[3 - int(coordinates[-1])][int(coordinates[0]) - 1]
    chosen_field = field[3 - int(coordinates[-1])][int(coordinates[0]) - 1]

    while chosen_field == 'X' or chosen_field == 'O':
        print('This cell is occupied! Choose another one!')
        coordinates = input()
        chosen_field = field[3 - int(coordinates[-1])][int(coordinates[0]) - 1]

    if move_counter % 2 != 0:
        field[3 - int(coordinates[-1])][int(coordinates[0]) - 1] = 'X'
    else:
        field[3 - int(coordinates[-1])][int(coordinates[0]) - 1] = 'O'

    move_counter += 1

    print_field()
    result()
