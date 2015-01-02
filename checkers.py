
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

def canMove(player,m,n):
	if player == 1:
		if board[m][n] == 1:
			if board[m+1][n+1] == 0 or board[m+1][n-1] == 0:
				return True
			elif board[m+1][n+1] == 2 and board[m+2][n+2] == 0:
				return True
			elif board[m+1][n-1] == 2 and board[m+2][n-2] == 0:
				return True
			else:
				return False
		else:
			return False
	elif player == 2:
		if board[m][n] == 1:
			if board[m-1][n+1] == 0 or board[m-1][n-1] == 0:
				return True
			elif board[m-1][n+1] == 1 and board[m-2][n+2] == 0:
				return True
			elif board[m-1][n-1] == 1 and board[m-2][n-2] == 0:
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


# for row in board:
	# print row

setupBoard()
printBoard()