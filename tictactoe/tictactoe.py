####################
# Tic Tac Toe
####################
import random

# Description

# TicTacToe Board
#
# | 7 | 8 | 9 | - Layer1
# | 4 | 5 | 6 | - Layer2
# | 1 | 2 | 3 | - Layer3
#

# Rules
# 1. Alternate X and O
# 2. Cannot overwrite existing block
# 3. Stop the game when a winning combination found
# 4. Outcomes : Win or Draw
#

# Globals
char_list = ['O','X']
board_layer = []
##################
# Helper Functions
##################

def reset_board():
    board_layer = ['0'] + list(range(1,10))
    print('\t| {} | {} | {} |'.format(board_layer[7],board_layer[8],board_layer[9]))
    print('\t| {} | {} | {} |'.format(board_layer[4],board_layer[5],board_layer[6]))
    print('\t| {} | {} | {} |'.format(board_layer[1],board_layer[2],board_layer[3]))
    return board_layer

def update_board(num,char,board_layer):

    board_layer[int(num)] = char

    print('\t| {} | {} | {} |'.format(board_layer[7],board_layer[8],board_layer[9]))
    print('\t| {} | {} | {} |'.format(board_layer[4],board_layer[5],board_layer[6]))
    print('\t| {} | {} | {} |'.format(board_layer[1],board_layer[2],board_layer[3]))
   
    return board_layer

def check_board_for_win(board_layer):
    #Conditions to win
    # Same values in index 123 456 789 147 258 369 159 753
    #Check Horizontals
    if len(set(board_layer[1:4])) == 1 or len(set(board_layer[4:7])) == 1 or len(set(board_layer[7:10])) == 1:
        return True
    #Check Verticals
    if len(set(board_layer[1:10:3])) == 1 or len(set(board_layer[2:10:3])) == 1 or len(set(board_layer[3:10:3])) == 1:
        return True
    #Check Diagonals
    if len(set(board_layer[1:10:4])) == 1 or len(set(board_layer[3:8:2])) == 1:
        return True
    
    return False
##################
# Main Program
##################


continue_play = True
while continue_play:
    #Get Input from User
    player1 = input("Enter Player 1 Name : ") # Player1
    player2 = input("Enter Player 2 Name : ") # Player2

    #Determine who will play first
    player_list = [player1,player2]
    random.shuffle(player_list)
    x = 0 #Player Index
    
    # Reset Values # Board Display
    board_layer = reset_board()

    # Main Game Execution
    someone_win = False
    total_input = 0

    while not someone_win:
        
        num = input(f'{player_list[x]} turn. Input Position (1-9) : ')
        #take the input 
        # check if input is a digit, within the range 1 - 9, and a position not yet taken
        while num.isdigit() == False or int(num) not in range(1,10) or board_layer[int(num)] in char_list:
            num = input("Position Taken or not Existing. Enter Again : ")
        #update and print the board
        board_layer = update_board(num,char_list[x],board_layer)
        
        someone_win = check_board_for_win(board_layer)
        total_input += 1
        
        if someone_win:
            print(f'{player_list[x]} Won!')
            break
        if total_input >= 9:
            print("It's a Draw!")
            break
        
        x = (x + 1) % 2 #shuffle between index 1 and 0

    #Ask for Another Game            
    play_again = input("Play Again? (Y/N): ")
    if play_again.lower() != 'y':
        continue_play = False
