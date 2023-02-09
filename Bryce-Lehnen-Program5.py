import numpy as np
import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      
# Program 5: DigiPeg Solitaire          
# Bryce Lehnen
# Last Modified: Nov 18, 2020               
# ---------------------------------------
# A peg game where to remove a peg, you must 'jump' over it with another peg
# ---------------------------------------

# ---------------------------------------
# Start of DigiPeg Class                
# ---------------------------------------

class DigiPeg:

    def __init__(self, rows, columns, empty_row, empty_col):
        self.board = np.full((rows, columns), True)
        self.board[empty_row][empty_col] = False
        self.pegs_left = rows * columns - 1
        
# ---------------------------------------

    def __str__(self):
        answer = "   "
        for column in range(self.board.shape[1]):
            answer += " " + str(column + 1) + "  "
        answer += "\n"
        answer += self.separator()
        for row in range(self.board.shape[0]):
            answer += str(row + 1) + " |"
            for col in range(self.board.shape[1]):
                if self.board[row][col]:
                    answer += " o |"
                else:
                    answer += "   |"
            answer += "\n"
            answer += self.separator()
        return answer
    
# ---------------------------------------

    def separator(self):
        answer = "  +"
        for _ in range(self.board.shape[1]):
            answer += "---+"
        answer += "\n"
        return answer

# ---------------------------------------

    def final_message(self):
        total_pegs = 0
          
        for row in range(self.board.shape[0]):
              for col in range(self.board.shape[1]):
                    if (self.board[row, col] == True):
                          total_pegs = total_pegs + 1
          
        if (total_pegs <= 2):
              print("You're a DigiPeg-enius!")
        elif (total_pegs == 3 or total_pegs == 4):
              print("I've worked with better. But not many.")
        elif (total_pegs == 5 or total_pegs == 5):
              print(tota_pegs, " left? Really? You're gonna have to do better than that.")
        elif (total_pegs >= 7):
              print("DigiPeg-naramous! Rack'em up and redeem yourself.")

# ---------------------------------------

    def game_over(self):
        for ROW in range(1, (self.board.shape[0] + 1)):
              for COL in range(1, (self.board.shape[1] + 1)):
                    peg = ""
                    row = ROW - 1
                    col = COL - 1

                    #- Adds restrictions for each peg
                    #- ie. A peg on the far left cannot check any of the left sided pegs thus removing 3/8 potential pegs
                    if (self.board[(ROW - 1), (COL - 1)] == True):
                          #- Top row
                          if (ROW == 1 or ROW == 2):
                                peg = peg + "T"
                          #- Bottom row
                          if (ROW == self.board.shape[0] or ROW == (self.board.shape[0] - 1)):
                                peg = peg + "B"
                          #- Left col
                          if (COL == 1 or COL == 2):
                                peg = peg + "L"
                          #- Right Col
                          if (COL == self.board.shape[1]or COL == (self.board.shape[1] - 1)):
                                peg = peg + "R"
                    else:
                          peg = "HOLE"

                    #- Checks positions around the designated peg
                    if (peg == ""):
                          #- Checks up
                          if (self.board[row-1, col] == True and self.board[row-2, col] == False):
                                return False
                          #- Checks down
                          if (self.board[row+1, col] == True and self.board[row+2, col] == False):
                                return False
                          #- Checks left
                          if (self.board[row, col-1] == True and self.board[row, col-2] == False):
                                return False
                          #- Checks right
                          if (self.board[row, col+1] == True and self.board[row, col+2] == False):
                                return False
                          #- Checks up, left
                          if (self.board[row-1, col-1] == True and self.board[row-2, col-2] == False):
                                return False
                          #- Checks up, right
                          if (self.board[row-1, col+1] == True and self.board[row-2, col+2] == False):
                                return False
                          #- Checks down, left
                          if (self.board[row+1, col-1] == True and self.board[row+2, col-2] == False):
                                return False
                          #- Checks down, right
                          if (self.board[row+1, col+1] == True and self.board[row+2, col+2] == False):
                                return False
                              
                    else:
                          #------------------------------------------------------------------------------
                          #- ALL 4 COMBO
                          if (peg == "TBLR"):
                                #- Peg cannot be moved
                                pass

                          #------------------------------------------------------------------------------
                          #- 3 RESTRICTIONS
                          if (peg == "TBL"):
                                #- Checks right
                                if (self.board[row, col+1] == True and self.board[row, col+2] == False):
                                      return False
                          if (peg == "TBR"):
                                #- Checks left
                                if (self.board[row, col-1] == True and self.board[row, col-2] == False):
                                      return False
                          if (peg == "BLR"):
                                #- Checks up
                                if (self.board[row-1, col] == True and self.board[row-2, col] == False):
                                      return False
                          if (peg == "TLR"):
                                #- Checks down
                                if (self.board[row+1, col] == True and self.board[row+2, col] == False):
                                      return False

                          #------------------------------------------------------------------------------       
                          #-- 2 RESTRICTIONS
                          #- Top
                          if (peg == "TB"):
                                #- Checks left
                                if (self.board[row, col-1] == True and self.board[row, col-2] == False):
                                      return False
                                #- Checks right
                                if (self.board[row, col+1] == True and self.board[row, col+2] == False):
                                      return False
                          if (peg == "TL"):
                                #- Checks down
                                if (self.board[row+1, col] == True and self.board[row+2, col] == False):
                                      return False
                                #- Checks right
                                if (self.board[row, col+1] == True and self.board[row, col+2] == False):
                                      return False
                                #- Checks down, right
                                if (self.board[row+1, col+1] == True and self.board[row+2, col+2] == False):
                                      return False
                          if (peg == "TR"):
                                #- Checks down
                                if (self.board[row+1, col] == True and self.board[row+2, col] == False):
                                      return False
                                #- Checks left
                                if (self.board[row, col-1] == True and self.board[row, col-2] == False):
                                      return False
                                #- Checks down, left
                                if (self.board[row+1, col-1] == True and self.board[row+2, col-2] == False):
                                      return False
                          #- Bottom
                          if (peg == "BL"):
                                #- Checks up
                                if (self.board[row-1, col] == True and self.board[row-2, col] == False):
                                      return False
                                #- Checks right
                                if (self.board[row, col+1] == True and self.board[row, col+2] == False):
                                      return False
                                #- Checks up, right
                                if (self.board[row-1, col+1] == True and self.board[row-2, col+2] == False):
                                      return False
                          if (peg == "BR"):
                                #- Checks up
                                if (self.board[row-1, col] == True and self.board[row-2, col] == False):
                                      return False
                                #- Checks left
                                if (self.board[row, col-1] == True and self.board[row, col-2] == False):
                                      return False
                                #- Checks up, left
                                if (self.board[row-1, col-1] == True and self.board[row-2, col-2] == False):
                                      return False
                          #- Left, right
                          if (peg == "LR"):
                                #- Checks up
                                if (self.board[row-1, col] == True and self.board[row-2, col] == False):
                                      return False
                                #- Checks down
                                if (self.board[row+1, col] == True and self.board[row+2, col] == False):
                                      return False

                          #------------------------------------------------------------------------------
                          #- 1 RESTRICTIONS
                          if (peg == "T"):
                                #- Checks down
                                if (self.board[row+1, col] == True and self.board[row+2, col] == False):
                                      return False
                                #- Checks left
                                if (self.board[row, col-1] == True and self.board[row, col-2] == False):
                                      return False
                                #- Checks right
                                if (self.board[row, col+1] == True and self.board[row, col+2] == False):
                                      return False
                                #- Checks down, left
                                if (self.board[row+1, col-1] == True and self.board[row+2, col-2] == False):
                                      return False
                                #- Checks down, right
                                if (self.board[row+1, col+1] == True and self.board[row+2, col+2] == False):
                                      return False
                          if (peg == "B"):
                                #- Checks up
                                if (self.board[row-1, col] == True and self.board[row-2, col] == False):
                                      return False
                                #- Checks left
                                if (self.board[row, col-1] == True and self.board[row, col-2] == False):
                                      return False
                                #- Checks right
                                if (self.board[row, col+1] == True and self.board[row, col+2] == False):
                                      return False
                                #- Checks up, left
                                if (self.board[row-1, col-1] == True and self.board[row-2, col-2] == False):
                                      return False
                                #- Checks up, right
                                if (self.board[row-1, col+1] == True and self.board[row-2, col+2] == False):
                                      return False
                          if (peg == "L"):
                                #- Checks up
                                if (self.board[row-1, col] == True and self.board[row-2, col] == False):
                                      return False
                                #- Checks down
                                if (self.board[row+1, col] == True and self.board[row+2, col] == False):
                                      return False
                                #- Checks right
                                if (self.board[row, col+1] == True and self.board[row, col+2] == False):
                                      return False
                                #- Checks up, right
                                if (self.board[row-1, col+1] == True and self.board[row-2, col+2] == False):
                                      return False
                                #- Checks down, right
                                if (self.board[row+1, col+1] == True and self.board[row+2, col+2] == False):
                                      return False
                                
                          if (peg == "R"):
                                #- Checks up
                                if (self.board[row-1, col] == True and self.board[row-2, col] == False):
                                      return False
                                #- Checks down
                                if (self.board[row+1, col] == True and self.board[row+2, col] == False):
                                      return False
                                #- Checks left
                                if (self.board[row, col-1] == True and self.board[row, col-2] == False):
                                      return False
                                #- Checks up, left
                                if (self.board[row-1, col-1] == True and self.board[row-2, col-2] == False):
                                      return False
                                #- Checks down, left
                                if (self.board[row+1, col-1] == True and self.board[row+2, col-2] == False):
                                      return False
                  
        return True

# ---------------------------------------

    def legal_move(self, row_start, col_start, row_end, col_end):
        #- Checks to see if start has a peg and end is empty
        if (self.board[row_start, col_start] == True and self.board[row_end, col_end] == False):
              #- CHECKS UP, DOWN, LEFT, RIGHT MOVES
              #- Checks if start and end are spaced apart properlly
              if (abs(row_start - row_end) == 2):
                    #- Logic for orientating pegs
                    if ((row_start > row_end) and (col_start == col_end)):
                          #- The final check if space in-between has a peg
                          if (self.board[(row_start - 1), col_start]):
                                return True
                    elif ((row_end > row_start) and (col_start == col_end)):
                          if (self.board[(row_start + 1), col_start]):
                                return True
              elif (abs(col_start - col_end) == 2):
                    if ((col_start > col_end) and (row_start == row_end)):
                          if (self.board[row_start, (col_start - 1)]):
                                return True
                    elif ((col_end > col_start) and (row_start == row_end)):
                          if (self.board[row_start, (col_start + 1)]):
                                return True

              #- CHECKS DIAGONAL MOVES
              #- Checks if start and end are spaced apart properlly
              if ((abs(row_start - row_end) == 2) and (abs(col_start - col_end) == 2)):
                    #- Logic to orientate pegs
                    #- Moves down and left
                    if ((row_start > row_end) and (col_start > col_end)):
                          #- The final check if space in-between has a peg
                          if (self.board[(row_start - 1), (col_start - 1)]):
                                return True
                    #- Moves up and left
                    elif ((row_start > row_end) and (col_start < col_end)):
                          if (self.board[(row_start - 1), (col_start + 1)]):
                                return True
                    #- Moves down and right
                    elif ((row_start < row_end) and (col_start > col_end)):
                          if (self.board[(row_start + 1), (col_start - 1)]):
                                return True
                    #- Moves up and right
                    elif ((row_start < row_end) and (col_start < col_end)):
                          if (self.board[(row_start + 1), (col_start + 1)]):
                                return True

        return False

# ---------------------------------------

    def make_move(self, row_start, col_start, row_end, col_end):
        #- Assigns the peg to be removed
        #- Checks up, down, left, right
        if ((row_start > row_end) and (col_start == col_end)):
              adj_row = row_start - 1
              adj_col = col_start
        elif ((row_start < row_end) and (col_start == col_end)):
              adj_row = row_start + 1
              adj_col = col_start
        elif ((col_start > col_end) and (row_start == row_end)):
              adj_row = row_start
              adj_col = col_start - 1
        elif ((col_start < col_end) and (row_start == row_end)):
              adj_row = row_start
              adj_col = col_start + 1
        #- Checks diagonal
        elif ((row_start > row_end) and (col_start > col_end)):
              adj_row = row_start - 1
              adj_col = col_start - 1
        elif ((row_start > row_end) and (col_start < col_end)):
              adj_row = row_start - 1
              adj_col = col_start + 1
        elif ((row_start < row_end) and (col_start > col_end)):
              adj_row = row_start + 1
              adj_col = col_start - 1
        elif ((row_start < row_end) and (col_start < col_end)):
              adj_row = row_start + 1
              adj_col = col_start + 1

        #- Removes and moves pegs
        self.board[row_start, col_start] = False
        self.board[row_end, col_end] = True
        self.board[adj_row, adj_col] = False

# ---------------------------------------
# End of DigiPeg Class               
# ---------------------------------------

def get_choice(low, high, message):
    message += " [" + str(low) + " - " + str(high) + "]: "
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    print("Welcome to DigiPeg Solitaire!")
    print("-----------------------------------\n")
    
    rows = get_choice(1, 9, "Enter the number of rows")
    columns = get_choice(1, 9, "Enter the number of columns")
    row = get_choice(1, rows, "Enter the empty space row") - 1
    column = get_choice(1, columns, "Enter empty space column") - 1   
    game = DigiPeg(rows, columns, row, column)
    print()

    print(game)
    while (not game.game_over()):
        row_start = get_choice(1, rows, "Enter the row of the peg to move") - 1
        col_start = get_choice(1, columns, "Enter the column of the peg to move") - 1
        row_end = get_choice(1, rows, "Enter the row where the peg lands") - 1
        col_end = get_choice(1, columns, "Enter the column where the peg lands") - 1
        if game.legal_move(row_start, col_start, row_end, col_end):
            game.make_move(row_start, col_start, row_end, col_end)
        else:
            print("Sorry.  That move is not allowed.")
        print()
        print(game)

    game.final_message()

# ---------------------------------------

main()
