from sys import exit

board = [[0 for i in xrange(8)] for i in xrange(8)]


def setupBoard():
	'Sets up the board to play checkers'
	for m in xrange(8):
		if m%2 == 0:
			board[0][m] = 1
			board[2][m] = 1
			board[6][m] = 2
		else:
			board[1][m] = 1
			board[5][m] = 2
			board[7][m] = 2

def printBoard():
	'Prints the current board configuration'
	for n in xrange(8):
		pRow = ''
		for m in xrange(8):
			if board[n][m] == 0:
				if (n+m)%2 == 0:
					pRow += '. '
				else:
					pRow += '  '
			elif board[n][m] == 1:
				pRow += 'X '
			elif board[n][m] == 2:
				pRow += 'O '
		print pRow

def canMove(player,n,m):
	if n > 7 or n < 0 or m > 7 or m < 0:
		return False
	if player == 1:
		if board[n][m] == 1:
			if board[(n+1)%8][(m+1)%8] == 0 or board[(n+1)%8][(m-1)%8] == 0:
				return True
			elif board[(n+1)%8][(m+1)%8] == 2 and board[(n+2)%8][(m+2)%8] == 0:
				return True
			elif board[(n+1)%8][(m-1)%8] == 2 and board[(n+2)%8][(m-2)%8] == 0:
				return True
	elif player == 2:
		if board[n][m] == 2:
			if board[(n-1)%8][(m+1)%8] == 0 or board[(n-1)%8][(m-1)%8] == 0:
				return True
			elif board[(n-1)%8][(m+1)%8] == 1 and board[(n-2)%8][(m+2)%8] == 0:
				return True
			elif board[(n-1)%8][(m-1)%8] == 1 and board[(n-2)%8][(m-2)%8] == 0:
				return True
	return False

def isLegalMove(player, n, m, a, b):
	if player != 1 and player != 2:
		return False
	if n > 7 or n < 0 or m > 7 or n < 0 or a > 7 or a < 0 or b > 7 or b < 0:
		return False
	if board[a][b] == 0:	
		if player == 1 and board[n][m] == 1:
			if a == (n+1)%8 and (b == (m+1)%8 or b == (m-1)%8):
				return True
			elif a == (n+2)%8 and b == (m+2)%8 and board[(n+1)%8][(m+1)%8] == 2:
				return True
			elif a == (n+2)%8 and b == (m-2)%8 and board[(n+1)%8][(m-1)%8] == 2:
				return True
		elif player == 2 and board[n][m] == 2:
			if a == (n-1)%8 and (b == (m+1)%8 or b == (m-1)%8):
				return True
			elif a == (n-2)%8 and b == (m+2)%8 and board[(n-1)%8][(m+1)%8] == 1:
				return True
			elif a == (n-2)%8 and b == (m-2)%8 and board[(n-1)%8][(m-1)%8] == 1:
				return True
	return False

def checkWinner():
	'Checks if there is a winner'
	p1 = True
	p2 = True

	for row in xrange(8):
		for col in xrange(8):
			if p2 and board[row][col] == 1 and canMove(1,row,col):
				# print('p2 {0} {1}'.format(row, col))
				p2 = False
			elif p1 and board[row][col] == 2 and canMove(2,row,col):
				# print('p1 {0} {1}'.format(row, col))
				p1 = False

	if p1:
		return 1
	elif p2:
		return 2
	return 0

def makeMove(player,n,m,a,b):
	board[n][m] = 0
	board[a][b] = player
	if (a+n)%2 == 0:
		if a == (n+2)%8:
			row = (n+1)%8
		else:
			row = (n-1)%8
		if b == (m+2)%8:
			col = m+1
		else:
			col = m-1
		board[row][col] = 0

def getInput(player):
	move = str(raw_input('\n Player {}:'.format(player)))
	if move == 'q' or move == 'quit':
		exit(0)
	if len(move) != 4:
		print('\n Illegal Move! \nPlease provide a legal move.\n')
		return player
	n, m = int(move[0]), int(move[1])
	a, b = int(move[2]), int(move[3])
	if isLegalMove(player,n,m,a,b):
		makeMove(player,n,m,a,b)
		newPlayer = player+1
		if newPlayer > 2:
			newPlayer -= 2
		return newPlayer
	else:
		print('\n Illegal Move! \nPlease provide a legal move.\n')
		return player


setupBoard()
printBoard()

pl = 1
while (1>0):
	pl = getInput(pl)
	printBoard()
	winner = checkWinner()
	if winner == 1:
		print(' Player 1 Wins!')
		break
	elif winner == 2:
		print(' Player 2 Wins!')
		break

