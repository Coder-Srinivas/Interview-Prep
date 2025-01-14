from board import Board

board = Board(4, 2)

while board.winner == None:
    try:
        board.printBoard()
        row, col = input("Where would you like to place ").split(" ")
        row = int(row)
        col = int(col)
        board.move(row, col)
        board.printBoard()
    except Exception as e:
        print("Incorrect input. Try again")