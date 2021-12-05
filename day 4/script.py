# day 1
# what 

print("Part 1 \n  ------------------------------------")


with open("input.txt", "r") as file:
    contents = file.read()
    sections = contents.split("\n\n")
    numbers = [int(num) for num in sections[0].split(",")]
    boards_raw = sections[1:]
    boards = []
    for board_raw in boards_raw:
        rows_raw = board_raw.split("\n")
        board = []
        for row_raw in rows_raw:
            row = [int(num) for num in row_raw.split()]
            board.append(row)
        boards.append(board)
