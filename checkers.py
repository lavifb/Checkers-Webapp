
board = [[0]*8]*8




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