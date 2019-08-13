test_board = ["x","o","x","o","x","o","x","o","x"]
board = [" "]*10

def display_board(board):
	print('\n'*100)
	print(board[7] + "|" + board[8] + "|" + board[9])
	print(board[4] + "|" + board[5] + "|" + board[6])
	print(board[1] + "|" + board[2] + "|" + board[3])
	
def player_input():
	marker = ""
	while marker != "X" and marker != "O":
		marker = input("Player 1: Choose X or O! ").upper()
		player1 = marker
		
	if marker == "X":
		player2 = "O"
	else:
		player2 = "X"
		
	return (player1,player2)
	

player1_marker, player2_marker = player_input()
print("Player 1 chose" + player1_marker + ", Player 1 goes first.")
turn = 1    
total_turns = 0
marker = ""
identifier = 0  
position = 0

while total_turns != 9:
	if board[9] == board[7] == board[8] == marker or board[6] == board[4] == board[5] == marker or board[3] == board[1] == board[2] == marker:
		print("Player" + str(identifier) + "Wins")
		break
	if turn == 1:
		display_board(board)
		while board[position] != ' ' or position not in [1,2,3,4,5,6,7,8,9]:
			position = int(input("Player 1:Where would you like to place your marker?"))
			board[position] = player1_marker
			marker = player1_marker
			display_board(board)
			turn = 2
			total_turns += 1
			identifier = 1
	
	elif turn == 2:
		display_board(board)
		while board[position] != ' ' or position not in [1,2,3,4,5,6,7,8,9]:
			position = int(input("Player 2:Where would you like to place your marker?"))
			board[position] = player2_marker
			current_marker = player2_marker
			marker = player2_marker
			display_board(board)
			turn = 1	
			total_turns += 1
			identifier = 2
		
else:
	print("It's a tie!")
