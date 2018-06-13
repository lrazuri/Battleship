from random import randint

#Makes the board
def Board_maker(Dimx,Dimy):
    board = []
    for x in range(0, Dimx):
        board.append(["O"] * Dimy)
    return (board)

#prints the boards
def print_board(board):
    for row in board:
        print (" ".join(row))

def B_Ship_game(Dimx,Dimy):
    #Checks how many players
    Players=input("How many people are playing?(1 or 2 only) ")
    while Players.isnumeric()==False or int(Players) >= 3: 
        print("Type the numbers 1 or 2")
        Players=input("How many people are playing?(1 or 2 only)")    
    #Checks how many turns each player
    Turn_number=input("How many turns will each player get? ")
    while Turn_number.isnumeric()==False or int(Turn_number) <= 17 or int(Turn_number)>Dimx*Dimy: 
        print("Made a mistake, Type a number that is greater than 17 or less than "+str(Dimx*Dimy))
        Turn_number=input("How many turns will each player get? ")
        
    ships=["Carrier","Battleship","Cruiser","Submarine","Destroyer"]
    shipspace=[5,4,3,3,2]
    initials=["C","B","C","S","D"]
    
    #one player game
    if int(Players) == 1:
        board = Board_maker(Dimx,Dimy)
        print_board(board)
        
        def random_row(board):
            return randint(0, len(board) - 1)
        def random_col(board):
            return randint(0, len(board[0]) - 1)
        
        ship_row = random_row(board)
        ship_col = random_col(board)
        print (ship_row)
        print (ship_col)
        
        for turn in range(Dimx**2):
            print ("Turn", turn + 1)
            guess_row = input("Guess Row: ")
            guess_col = input("Guess Col: ")
            #makes sure numerical value, #makes sure it is on the board #makes sure it is not a repeat
            while guess_row.isnumeric()==False or guess_col.isnumeric()==False or \
            int(guess_row) >= len(board) or int(guess_col) >= len(board[0]) or \
            board[int(guess_row)][int(guess_col)] == "X": 
                print( "Your input is not valid, try again" )
                guess_row = input("Guess Row: ")
                guess_col = input("Guess Col: ")
                                           
            if int(guess_row) == ship_row and int(guess_col) == ship_col:
                print ("Congratulations! You sank my battleship!")  
                break
            else: 
                print ("You missed my battleship!")
                board[int(guess_row)][int(guess_col)] = "X"
                print_board(board)     
                
    #2 player game
    else:
        board1 = Board_maker(Dimx,Dimy)
        Rboard1= Board_maker(Dimx,Dimy)
        board2 = Board_maker(Dimx,Dimy)
        Rboard2= Board_maker(Dimx,Dimy)
        print("Player 1 place ships now:")
        for ship,space,ini in zip(ships,shipspace,initials):
            print(str(ship)+"s have "+str(space)+" spots where do you want to put it")
            for i in range(space):
                print("Place point " + str(i+1) + " of ship")
                P1boat_row=int(input("Which row will your boat be in? "))
                P1boat_col=int(input("Which collumn will your boat be in? "))
                Rboard1[int(P1boat_row)][int(P1boat_col)] = ini
                print_board(Rboard1)
        print ("\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n")
        print('Let player 2 choose their ships location now')
        print("Player 2 place ships now:")
        for ship,space,ini in zip(ships,shipspace,initials):
            print(str(ship)+"s have "+str(space)+" spots where do you want to put it")
            for i in range(space):
                print("Place point " + str(i+1) + " of ship")
                P2boat_row=int(input("Which row will your boat be in? "))
                P2boat_col=int(input("Which collumn will your boat be in? "))
                Rboard2[int(P2boat_row)][int(P2boat_col)] = ini
                print_board(Rboard2)
        print ("\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n" "\n")
        
        for turn in range(Turn_number*2):
            if turn % 2==0:
                print ("Player 1, Turn", turn//2 + 1)
                guess_row = input("Guess Row: ")
                guess_col = input("Guess Col: ")
                #makes sure numerical value, #makes sure it is on the board #makes sure it is not a repeat
                while guess_row.isnumeric()==False or guess_col.isnumeric()==False or \
                int(guess_row) >= len(board2) or int(guess_col) >= len(board2[0]) or \
                board2[int(guess_row)][int(guess_col)] == "X": 
                    print( "Your input is not valid, try again" )
                    guess_row = input("Guess Row: ")
                    guess_col = input("Guess Col: ")
                                               
                if Rboard2[int(guess_row)][int(guess_col)] != "O":
                    print ("You hit one of my ships")
                    board2[int(guess_row)][int(guess_col)] = "H"
                    print_board(board2) 
                else: 
                    print ("You missed my battleship!")
                    board2[int(guess_row)][int(guess_col)] = "X"
                    print_board(board2)        
            else:
                print ("Player 2, Turn", turn//2 + 1)
                guess_row = input("Guess Row: ")
                guess_col = input("Guess Col: ")
                #makes sure numerical value, #makes sure it is on the board #makes sure it is not a repeat
                while guess_row.isnumeric()==False or guess_col.isnumeric()==False or \
                int(guess_row) >= len(board1) or int(guess_col) >= len(board1[0]) or \
                board1[int(guess_row)][int(guess_col)] == "X": 
                    print( "Your input is not valid, try again" )
                    guess_row = input("Guess Row: ")
                    guess_col = input("Guess Col: ")
                                               
                if Rboard1[int(guess_row)][int(guess_col)] != "O":
                    print ("You hit one of my ships")
                    board1[int(guess_row)][int(guess_col)] = "H"
                    print_board(board1)
                else: 
                    print ("You missed my battleship!")
                    board1[int(guess_row)][int(guess_col)] = "X"
                    print_board(board1)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        