import random

# 
# NAME: IKECHUKWU 
#


print("This is for IMC ONLINE CODE ASSESMENT  NAME: IKECHUKWU KENNETH ANABA")
print("                                                                    ")
print("NAME: IKECHUKWU KENNETH ANABA")
print("                                                                    ")
print("Two players are meant to play this game both players enters their names the the random code selects at random which to start")


# choice = input(input("How many row and column board do you want? Please chose a number between 5 and 10 because large numbers will make the game more difficult for you" ))
       

valid = [str(i) for i in range(-10,11)]

p = input("How many row and column board do you want? Please chose a number between 1 and 10 because large numbers will make the game more difficult for you: ")
countE=0
while p not in valid:
    if countE>0:
        print ("Please try to behave yourself and obey the rules of the game! Remember every game has a rule!")
    p = input("Not valid. Try to enter a number again: ")
    countE=countE+1



p = int(p)   
print ("Awsome! Good player!!  You selected "+str(p))
def rowDraw(p):
   for x in range(0,p):
    print(x, end=" ")
   print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")  
    #This prints  numbers from 0 to the selected number for design





board = []
# this is for board drawing
for x in range(0,p):
  board.append(["o"] * p)
  #This draw a vertical line with o

def print_board(board):

  rowDraw(p) 
  for row in board:
    print (" ".join(row))
    #This draw a horozontal join line with o




player_1 = input("Player 1 please enter your name: ")

player_2 = input("Player 2 please enter your name: ")

#This takes the both players name

players = [player_1, player_2]

#This stores the players names in an array

def random_player(players):
    return random.choice(players)

def random_row(board):
  return random.randint(0,len(board)-1)

def random_col(board):
  return random.randint(0,len(board[0])-1)

if random_player(players) == player_1:
  print(player_1, "starts the game.")
else:
  print(player_2, "starts the game.")
  

ship_row_1 = random_row(board)
#this  prints ship_row_1
ship_col_1 = random_col(board)
# this print ship_col_1
ship_row_2 = random_row(board)
#this  prints ship_row_2
ship_col_2 = random_col(board)
# this print ship_col_2

print_board(board)



player_start = random_player(players)




hit_count = 0
#The game begins here
for turn in range(p):
     guess_row = int(input("Guess Row: (allowed values: 0- "+str(p)+")"))
     
     guess_col = int(input("Guess Col: (allowed values: 0- "+str(p)+")"))

     if (guess_row == ship_row_1 and guess_col == ship_col_1) or (guess_row == ship_row_2 and guess_col == ship_col_2):
            hit_count = hit_count + 1
            board[guess_row][guess_col] = "*"
            print ("Congratulations! ")
            if hit_count == 1:
                   print("You sunk first battleship!") 
            elif hit_count == 2:
                   print("You sunk second battleship! You win!")
                   rowDraw(p)
                   print_board(board)
                   break
     else:
            if (guess_row < 0 or guess_row > p)  or (guess_col < 0 or guess_col > p):
                   print ("you entered a number out the range, please be obedient!")
            elif(board[guess_row][guess_col] == "X"):
                   print ("Hey! warrior you had entered that spot of number already, Please responsible! ")
            else:
                 print ("HAHAHHAHA! you missed my battleship! try being calculative!")
                 board[guess_row][guess_col] = "X"
            print (turn + 1, "turn")

     
     print_board(board)
print ("Ship 1 is hidden:")    
print (ship_row_1)
print (ship_col_1)

print ("Ship 2 is hidden:")    
print (ship_row_2)
print (ship_col_2)
board()
