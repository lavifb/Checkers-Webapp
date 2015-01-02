
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


# for row in board:
	# print row

setupBoard()
printBoard()
# print checkWinner()