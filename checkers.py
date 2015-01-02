
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

def checkWinner():
	'Checks if there is a winner'
	p1 = True
	p2 = True

	for row in board:
		for spot in row:
			if spot == 1:
				p2 = False
			elif spot == 2:
				p1 = False

	if p1:
		return 1
	elif p2:
		return 2
	return 0

def getInput(player):
	move = input('\n Player {}:'.format(player))
	n, m = move/1000%10, move/100%10
	a, b = move/10%10, move%10
	if isLegalMove(player,n,m,a,b):
		board[n][m] = 0
		board[a][b] = player
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
while (1<0):
	pl = getInput(pl)
	if checkWinner() == 1:
		print('Player 1 Wins!')
	elif checkWinner() == 2:
		print('Player 2 Wins!')