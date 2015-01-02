
board = [[0 for i in xrange(8)] for i in xrange(8)]


for m in xrange(8):
	if m%2 == 0:
		board[0][m] = 1
		board[2][m] = 1
		board[6][m] = 2
	else:
		board[1][m] = 1
		board[5][m] = 
		board[7][m] = 2




def printBoard():
	for row in board:
		pRow = ''
		for spot in row:
			if spot == 0:
				pRow += '.'
			elif spot == 1:
				pRow += 'X'
			elif spot == 2:
				pRow += 'O'
		print pRow



for row in board:
	print row

printBoard()
