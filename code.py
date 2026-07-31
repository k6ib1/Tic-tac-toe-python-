# board
# display board
# play game
# handle turn
# check win (rows, col, diag)
# check tie
# switch player

board = [["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]]

    

def displayboard():
    print(board[0][0] + "│" + board[0][1] + "│" + board[0][2])
    print(board[1][0] + "│" + board[1][1] + "│" + board[1][2])
    print(board[2][0] + "│" + board[2][1] + "│" + board[2][2])


displayboard()


def check_win():
    win = False
    for i in range(0,2):
        if board[i][0] == board[i][1] == board[i][2] and board[i][2] != "-":
            win = True
    for j in range(0,2):
        if board[0][j] == board[1][j] == board[2][j] and board[2][j] != "-":
            win = True
    return(win)



def play_game():
    stop = False
    while stop == False:
        print("Please assign player 1 and player 2 amoungst yourselves.")


        valid = False
        while valid == False:
            print("Player 1's turn")
            row = int(input("Enter desired row (0,1,2)"))
            col = int(input("Enter desired column (0,1,2)"))
            if board[row][col] == "-": 
                board[row][col] = "X"
                valid = True
            else:
                print("A player has already chosen this position\n Please try again.")
        print(displayboard())
        stop = check_win()
        if stop == True:
            print("Congrats player one!")

        
        valid = False
        while valid == False:
            print("Player 2's turn")
            row = int(input("Enter desired row (0,1,2)"))
            col = int(input("Enter desired column (0,1,2)"))
            if board[row][col] == "-": 
                board[row][col] = "O"
                valid = True
            else:
                print("A player has already chosen this position\n Please try again.")
        print(displayboard())
        stop = check_win()
        if stop == True:
            print("Congrats player two!")

play_game()
        
        
            
