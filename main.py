from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))
#print the ocean in 5x5 matrix 
print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

#ship_row and ship_col given random space in the ocean which player has to guess
ship_row = random_row(board)
ship_col = random_col(board)
#this comments are for testing
#print (ship_row)
#print (ship_col)


for turn in range(8):
  print ("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    #if the guess is right
    print ("Congratulations! You sank my battleship!")
    break
  else:
    #if the guess is out of range
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print ("Oops, that's not even in the ocean.")
    #if the guess is already made
    elif board[guess_row][guess_col] == "X":
      print ("You guessed that one already." )
    else:
      #if the guess is wrong
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    if (turn == 8):
      #when turn counter reaches 8, the game is over
      print ("Game Over")

print_board(board)
#THE END
