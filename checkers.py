
board = [[0 for i in xrange(8)] for i in xrange(8)]


def setupBoard():
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



# for row in board:
	# print row

setupBoard()
printBoard()
