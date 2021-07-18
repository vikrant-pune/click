import math


def for_Sec (sec):

    for i in range(1, 10):
        if sec.count(i) >= 2:
            print(f"Failed for Column  as {sec} ")
            return False
    else:
        return True

def check_for_place (board_set, r , c, num):

    # for given row
    if num in board_set[r] :
        return  False

    # for column
    column_rec = [row[c] for row in board_set]

    if num in column_rec:
        return False

    lower_bound_r = (math.floor (r / 3) ) * 3
    lower_bound_c = (math.floor(c /3) ) * 3


    sec_1 = [board_set[i][j] for (i, j) in [(i, j) for i in range(lower_bound_r, lower_bound_r + 3)
                                            for j in range(lower_bound_c, lower_bound_c +3)]]

    # print(sec_1)
    #
    # print(f"{lower_bound_r} and {lower_bound_c}")
    #
    # print([(i, j) for i in range(lower_bound_r, lower_bound_r + 3)
    #             for j in range(lower_bound_c, lower_bound_c +3)])
    if num in sec_1:
        return False
    return True

def is_valid (old_board_set , r=-1,c=-1,num = -1):

    board_set = old_board_set
    board_set[r][c] = num

    # draw_sudoku()
    # check Horizontal
    for r in range(len(board_set)):
        for i in range (1,10):
            if board_set[r].count(i) >= 2:
                print (f"Failed for Row {r}  as {board_set[r]}"  )
                board_set[r][c] = 0
                return False

    for c in range(len(board_set)):
        column_set = [row[c] for row in board_set]
        for i in range (1, 10):
            if column_set.count(i) >= 2:
                print(f"Failed for Column {c} as {column_set} ")
                board_set[r][c] = 0
                return  False

    # in sector
    sec_1 = [ board_set[i][j] for (i,j) in [(i,j) for i in range(3) for j in range(3)]]
    value_1 = sec_count(sec_1)

    if value_1 == False :
        board_set[r][c] = 0
        return False

    sec_2 = [board_set[i][j] for (i, j) in [(i, j) for i in range(3,6) for j in range(3)]]
    value_1 = sec_count(sec_2)

    if value_1 == False:
        board_set[r][c] = 0
        return False

    sec_3 = [board_set[i][j] for (i, j) in [(i, j) for i in range(6,9) for j in range(3)]]
    value_1 = sec_count(sec_3)

    if value_1 == False:
        board_set[r][c] = 0
        return False

    sec_4 = [board_set[i][j] for (i, j) in [(i, j) for i in range(3) for j in range(3,6)]]
    value_1 = sec_count(sec_4)

    if value_1 == False:
        board_set[r][c] = 0
        return False
    sec_5 = [board_set[i][j] for (i, j) in [(i, j) for i in range(3,6) for j in range(3,6)]]
    value_1 = sec_count(sec_5)

    if value_1 == False:
        board_set[r][c] = 0
        return False
    sec_6 = [board_set[i][j] for (i, j) in [(i, j) for i in range(6,9) for j in range(3,6)]]
    value_1 = sec_count(sec_6)

    if value_1 == False:
        board_set[r][c] = 0
        return False
    #
    sec_7 = [board_set[i][j] for (i, j) in [(i, j) for i in range(3) for j in range(6,9)]]
    value_1 = sec_count(sec_7)

    if value_1 == False:
        board_set[r][c] = 0
        return False
    sec_8 = [board_set[i][j] for (i, j) in [(i, j) for i in range(3,6) for j in range(6,9)]]
    value_1 = sec_count(sec_8)

    if value_1 == False:
        board_set[r][c] = 0
        return False
    sec_9 = [board_set[i][j] for (i, j) in [(i, j) for i in range(6,9) for j in range(6,9)]]
    value_1 = sec_count(sec_9)

    if value_1 == False:
        board_set[r][c] = 0
        return False
    #
    print("")
    board_set[r][c] = 0
    return True


def sec_count(sec_1):
    for i in range(1, 10):
        if sec_1.count(i) >= 2:
            print(f"Failed for Column  as {sec_1} ")
            return  False
    else:
        return True

def fill_n_backtrack(board_set , r = -1  , c = -1  , num = -1 ):
    for r in range (len(board_set)):
        for c in range (len(board_set)):
            if board_set[r][c] != 0:
                continue
            for num in range (1,10):
                # check if possible
                if (r==0 and c == 0 and num == 5 ):
                    print ("Why")
                    if (r == 0 and c == 1 ):
                        print("Y")
                check = check_for_place(board_set, r , c, num)
                if check:
                    # is valid, fill in
                    board_set[r][c] = num
                    # draw_sudoku(board_set)
                    value = fill_n_backtrack(board_set)
                    if value != True:
                        # print(f"Returned for {r} {c} with {num} hence reset")
                        board_set[r][c] = 0
                    else:
                        break
            else:
                return False
    return True


# Draw Sudoku0
def draw_sudoku(board_set):
    print ("_________________________________====")
    for row_place in range(len(board_set)):
        for column_place in range(len(board_set[row_place])):

            end_place = " " if ( column_place + 1 ) % 3 != 0 else " |"
            print ( "  " if board_set[row_place][column_place] == 0 else f" {board_set[row_place][column_place]}", end = end_place)
        seprator = [ '_' for i in range (9)]

        if (row_place + 1 ) % 3 == 0:
            print( " ")
            for _ in seprator:
                print ( " _" , end = " ")
            else:
                print (" ")
        else:
            print (" ")
        # print(" " if row_place % 3  != 0  else seprator)


if __name__ == '__main__':
    board_set = [
                 [int(i) for i in "000104000" ],
                 # [int(i) for i in "235164700"],
                 [int(i) for i in "001000800"],
                 [int(i) for i in "080703060"],

                 [int(i) for i in "907000106"],
                 [int(i) for i in "000000000"],
                 [int(i) for i in "304000508"],

                 [int(i) for i in "050206030"],
                 [int(i) for i in "009000600"],
                 [int(i) for i in "000805000"],
                 # [0, 9, 0, 0, 8, 0, 1, 2, 3],
                ]
    #
    # board_set = [
    #     [int(i) for i in "596184327"],
    #     # [int(i) for i in "235164700"],
    #     [int(i) for i in "731620854"],
    #     [int(i) for i in "482753961"],
    #
    #     [int(i) for i in "927538146"],
    #     [int(i) for i in "815467293"],
    #     [int(i) for i in "364912578"],
    #
    #     [int(i) for i in "158246739"],
    #     [int(i) for i in "249371685"],
    #     [int(i) for i in "673090400"],
    #     # [0, 9, 0, 0, 8, 0, 1, 2, 3],
    # ]

    # board_set = [[int(i) for i in "100" ],
    #              [int(i) for i in "000"],
    #              [int(i) for i in "000"],
    #
    #             ]

    # print( check_for_place(board_set, 2,2,1))
    draw_sudoku(board_set)
    # is_valid(board_set)
    fill_n_backtrack(board_set)
    draw_sudoku(board_set)
