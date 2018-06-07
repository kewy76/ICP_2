# Kate Williams
# 6/7/2018


def horizontal(rows):
    print ("--- " * int(rows))


def vertical(cols):
    print("|  " * int(cols) + "|")


def board_draw(cols, rows):
    x = 0
    y = 0
    while x < int(rows):
        while y < int(cols):
            horizontal(rows)
            vertical(cols)
            y += 1
        x += 1
    horizontal(rows)


height = input("Enter the height of the board: ")
width = input("Enter the width of the board: ")
board_draw(height, width)
