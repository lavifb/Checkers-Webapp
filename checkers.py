
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

def canMove(player,m,n):
	if player == 1:
		if board[m][n] == 1:
			if board[(m+1)%8][(n+1)%8] == 0 or board[(m+1)%8][(n-1)%8] == 0:
				return True
			elif board[(m+1)%8][(n+1)%8] == 2 and board[(m+2)%8][(n+2)%8] == 0:
				return True
			elif board[(m+1)%8][(n-1)%8] == 2 and board[(m+2)%8][(n-2)%8] == 0:
				return True
			else:
				return False
		else:
			return False
	elif player == 2:
		if board[m][n] == 1:
			if board[(m-1)%8][(n+1)%8] == 0 or board[(m-1)%8][(n-1)%8] == 0:
				return True
			elif board[(m-1)%8][(n+1)%8] == 1 and board[(m-2)%8][(n+2)%8] == 0:
				return True
			elif board[(m-1)%8][(n-1)%8] == 1 and board[(m-2)%8][(n-2)%8] == 0:
				return True
			else:
				return False
		else:
			return False
	else:
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
			if board[row][col] == 1 and canMove(1,row,col):
				p2 = False
			elif board[row][col] == 2 and canMove(2,row,col):
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
		row = (n+a)/2
		col = (m+b)/2
		board[row][col] = 0

def getInput(player):
	move = input('\n Player {}:'.format(player))
	n, m = move/1000%10, move/100%10
	a, b = move/10%10, move%10
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
	if checkWinner() == 1:
		print('Player 1 Wins!')
	elif checkWinner() == 2:
		print('Player 2 Wins!')

