import time
from chessPlayer_queue import*

def getPiece (name):
	if (name=="pawn"):
		return 0
	elif (name=="knight"):
		return 1
	elif (name=="bishop"):
		return 2
	elif (name=="rook"):
		return 3
	elif (name=="queen"):
		return 4
	elif (name=="king"):
		return 5

def printPiece (piece):
	val=""
	if (piece-10==0):
		val="P[W]"
	elif (piece-20==0):
		val="P[B]"
	elif (piece-10==1):
		val="N[W]"
	elif (piece-20==1):
		val="N[B]"
	elif (piece-10==2):
		val="B[W]"
	elif (piece-20==2):
		val="B[B]"
	elif (piece-10==3):
		val="R[W]"
	elif (piece-20==3):
		val="R[B]"
	elif (piece-10==4):
		val="Q[W]"
	elif (piece-20==4):
		val="Q[B]"
	elif (piece-10==5):
		val="K[W]"
	elif (piece-20==5):
		val="K[B]"
	return val

def genBoard():
	r=[0]*64
	count=0
	white=10
	black=20
	for i in range (8,16):
		r[i]=white+getPiece("pawn")
		r[i+40]=black+getPiece("pawn")
	for x in range(0,2):
		r[x*56+0]=white+(x*10)+getPiece("rook")
		r[x*56+1]=white+(x*10)+getPiece("knight")
		r[x*56+2]=white+(x*10)+getPiece("bishop")
		r[x*56+3]=white+(x*10)+getPiece("king")
		r[x*56+4]=white+(x*10)+getPiece("queen")
		r[x*56+5]=white+(x*10)+getPiece("bishop")
		r[x*56+6]=white+(x*10)+getPiece("knight")
		r[x*56+7]=white+(x*10)+getPiece("rook")
	return r

def printBoard(board):
	accum="-----BLACK SIDE-----\n"
	max=63
	for j in range (0,8,1):
		for i in range(max-j*8,max-j*8-8,-1):
			accum=accum+'{0: <10}'.format(printPiece(board[i])+"["+str(i)+"]")
		accum=accum+"\n"
		accum = accum + "\n"
	accum=accum+"-----WHITE SIDE-----"
	return accum

def GetPlayerPositions (board,player):
	accum=[]
	for n in range (0,len(board)):
		if (player==10):
			if (board[n]<20 and board[n]>=10):
				accum=accum+[n]
		elif (player==20):
			if (board[n]>=20):
				accum=accum+[n]
	return accum

def removeFromList (x,val):
	accum=[]
	for n in range(0,len(x),1):
		if (x[n]!=val):
			accum=accum+[x[n]]
	return accum

def isInList(x,val):
	for n in range (0,len(x),1):
		if (x[n]==val):
			return True
	return False

def getPawnMoves (pos, playerSign, board, player):
	rightList = [0, 8, 16, 24, 32, 40, 48, 56]
	leftList = [7, 15, 23, 31, 39, 47, 55, 63]
	row1=[8,9,10,11,12,13,14,15]
	row6=[48,49,50,51,52,53,54,55]
	accum =[]
	#Check regular moves
	if (pos+8*playerSign>-1 and pos+8*playerSign<64):
		if (board[pos+8*playerSign]==0):
			accum=accum+[pos+8*playerSign]

	#if (player==10 and isInList(row1,pos)):
	#	if (pos + 16 * playerSign > -1 and pos + 16 * playerSign < 64):
	#		if (board[pos+16*playerSign]==0 and board[pos+8*playerSign]==0):
	#			accum=accum+[pos+16*playerSign]
	#elif (player==20 and isInList(row6,pos)):
	#	if (pos + 16 * playerSign > -1 and pos + 16 * playerSign < 64):
	#		if (board[pos+16*playerSign]==0 and board[pos+8*playerSign]==0):
	#			accum=accum+[pos+16*playerSign]

	#Check threaten moves
	if (pos + (8 * playerSign)+1 > -1 and pos + (8 * playerSign)+1 < 64):
		if (getPlayer(board,pos+(8*playerSign)+1)==10 and playerSign==-1 and isInList(rightList, pos+1)==False):
			accum=accum+[pos+(8*playerSign)+1]
		if (getPlayer(board,pos+(8*playerSign)+1)==20 and playerSign==1 and isInList(rightList, pos+1)==False):
			accum=accum+[pos+(8*playerSign)+1]

	if (pos + (8 * playerSign) - 1 > -1 and pos + (8 * playerSign) - 1 < 64):
		if (getPlayer(board,pos+(8*playerSign)-1)==10 and playerSign==-1 and isInList(leftList, pos-1)==False):
			accum=accum+[pos+(8*playerSign)-1]
		if (getPlayer(board,pos+(8*playerSign)-1)==20 and playerSign==1  and isInList(leftList, pos-1)==False):
			accum=accum+[pos+(8*playerSign)-1]

	return accum

def getKnightMoves (pos,playerSign,board,player):
	accum=[]
	rightList=[0,8,16,24,32,40,48,56]
	leftList=[7,15,23,31,39,47,55,63]
	col2List=[57,49,41,33,25,17,9,1]
	col7List=[62,54,46,38,30,22,14,6]
	
	if ((pos+16-1)<=63):
		if (getPlayer(board,pos+16-1)!=player):
			accum=accum+[pos+16-1]
	if ((pos+16+1)<=63):
		if (getPlayer(board,pos+16+1)!=player):			
			accum=accum+[pos+16+1]
	if ((pos-16+1)>=0):
		if (getPlayer(board,pos-16+1)!=player):
			accum=accum+[pos-16+1]
	if ((pos-16-1)>=0):
		if (getPlayer(board,pos-16-1)!=player):
			accum=accum+[pos-16-1]

	if ((pos+8+2)<=63):
		if (getPlayer(board,pos+8+2)!=player):
			accum=accum+[pos+8+2]
	if ((pos+8-2)<=63):
		if (getPlayer(board,pos+8-2)!=player):
			accum=accum+[pos+8-2]
	if ((pos-8-2)>=0):
		if (getPlayer(board,pos-8-2)!=player):
			accum=accum+[pos-8-2]
	if ((pos-8+2)>=0):
		if (getPlayer(board,pos-8+2)!=player):
			accum=accum+[pos-8+2]
	
	temp=accum
	for n in range(0,len(accum),1):
		if (isInList(leftList,accum[n]) and isInList(rightList,pos)):
			temp=removeFromList(temp,accum[n])
		if (isInList(rightList,accum[n]) and isInList(leftList,pos)):
			temp=removeFromList(temp,accum[n])

		if (isInList(leftList,accum[n]) and isInList(col2List,pos)):
			temp=removeFromList(temp,accum[n])
		if (isInList(rightList,accum[n]) and isInList(col7List,pos)):
			temp=removeFromList(temp,accum[n])

		if (isInList(col7List,accum[n]) and isInList(rightList,pos)):
			temp=removeFromList(temp,accum[n])
		if (isInList(col2List,accum[n]) and isInList(leftList,pos)):
			temp=removeFromList(temp,accum[n])

	return temp

def getRookMoves(pos, playerSign,board,player):
	accum=[]
	rightList = [0, 8, 16, 24, 32, 40, 48, 56]
	leftList = [7, 15, 23, 31, 39, 47, 55, 63]
	for n in range (pos+8,64,8):
		if (board[n]==0):
			accum=accum+[n]
		elif(getPlayer(board,n)==player):
			break
		elif(getPlayer(board,n)!=0 and getPlayer(board,n)!=player):
			accum=accum+[n]
			break
	for n in range (pos-8,-1,-8):
		if (board[n]==0):
			accum=accum+[n]
		if (getPlayer(board,n)==player):
			break
		elif (getPlayer(board,n)!=0 and getPlayer(board,n)!=player):
			accum = accum + [n]
			break
	for n in range (pos+1,63,1):
		if (isInList(rightList,n)):
			break
		if (board[n]==0):
			accum=accum+[n]
		if (getPlayer(board,n)==player):
			break
		elif (getPlayer(board,n)!=0 and getPlayer(board,n)!=player):
			accum = accum + [n]
			break
	for n in range (pos-1,-1,-1):
		if (isInList(leftList,n)):
			break
		if (board[n]==0):
			accum=accum+[n]
		if (getPlayer(board,n)==player):
			break
		elif (getPlayer(board,n)!=0 and getPlayer(board,n)!=player):
			accum = accum + [n]
			break
	return accum

def getBishopMoves(pos,playerSign,board,player):
	accum = []
	rightList = [0, 8, 16, 24, 32, 40, 48, 56]
	leftList = [7, 15, 23, 31, 39, 47, 55, 63]
	for n in range(pos + 9, 64, 9):
		if (isInList(rightList, n)):
			break
		if (board[n] == 0):
			accum = accum + [n]
		elif (getPlayer(board, n) == player):
			break
		elif (getPlayer(board, n) != 0 and getPlayer(board, n) != player):
			accum = accum + [n]
			break
	for n in range(pos - 9, -1, -9):
		if (isInList(leftList, n)):
			break
		if (board[n] == 0):
			accum = accum + [n]
		if (getPlayer(board, n) == player):
			break
		elif (getPlayer(board, n) != 0 and getPlayer(board, n) != player):
			accum = accum + [n]
			break
	for n in range(pos + 7, 63, 7):
		if (isInList(leftList, n)):
			break
		if (board[n] == 0):
			accum = accum + [n]
		if (getPlayer(board, n) == player):
			break
		elif (getPlayer(board, n) != 0 and getPlayer(board, n) != player):
			accum = accum + [n]
			break
	for n in range(pos - 7, -1, -7):
		if (isInList(rightList, n)):
			break
		if (board[n] == 0):
			accum = accum + [n]
		if (getPlayer(board, n) == player):
			break
		elif (getPlayer(board, n) != 0 and getPlayer(board, n) != player):
			accum = accum + [n]
			break
	return accum

def getQueenMoves (pos,playerSign,board,player):
	accum=getBishopMoves(pos,playerSign,board,player)+getRookMoves(pos,playerSign,board,player)
	return accum

def getKingMoves (pos,playerSign,board,player):
	rightList = [0, 8, 16, 24, 32, 40, 48, 56]
	leftList = [7, 15, 23, 31, 39, 47, 55, 63]
	accum=[]
	if ((pos+1)<64 and isInList(rightList, pos+1)==False):
		if (board[pos+1] == 0):
			accum = accum + [pos+1]
		elif (getPlayer(board, pos+1) != 0 and getPlayer(board, pos+1) != player):
			accum = accum + [pos+1]
	if ((pos -1) >-1 and isInList(leftList, pos -1) == False):
		if (board[pos-1] == 0):
			accum = accum + [pos-1]
		elif (getPlayer(board, pos-1) != 0 and getPlayer(board, pos-1) != player):
			accum = accum + [pos-1]

	if ((pos + 8) < 64):
		if (board[pos+8] == 0):
			accum = accum + [pos+8]
		elif (getPlayer(board, pos+8) != 0 and getPlayer(board, pos+8) != player):
			accum = accum + [pos+8]
	if ((pos - 8) >-1):
		if (board[pos-8] == 0):
			accum = accum + [pos-8]
		elif (getPlayer(board, pos-8) != 0 and getPlayer(board, pos-8) != player):
			accum = accum + [pos-8]

	if ((pos + 9) < 64 and isInList(rightList, pos + 9) == False):
		if (board[pos+9] == 0):
			accum = accum + [pos+9]
		elif (getPlayer(board, pos+9) != 0 and getPlayer(board, pos+9) != player):
			accum = accum + [pos+9]
	if ((pos - 9) >-1 and isInList(leftList, pos - 9) == False):
		if (board[pos-9] == 0):
			accum = accum + [pos-9]
		elif (getPlayer(board, pos-9) != 0 and getPlayer(board, pos-9) != player):
			accum = accum + [pos-9]

	if ((pos + 7) < 64 and isInList(leftList, pos + 7) == False):
		if (board[pos+7] == 0):
			accum = accum + [pos+7]
		elif (getPlayer(board, pos+7) != 0 and getPlayer(board, pos+7) != player):
			accum = accum + [pos+7]
	if ((pos - 7) >-1 and isInList(rightList, pos - 7) == False):
		if (board[pos-7] == 0):
			accum = accum + [pos-7]
		elif (getPlayer(board, pos-7) != 0 and getPlayer(board, pos-7) != player):
			accum = accum + [pos-7]
	return accum

def GetPieceLegalMoves (board,position):
	accum=[]
	if (getPlayer(board,position)==10):
		playerSign=1
		player=10
	else:
		playerSign=-1
		player=20
	if ((board[position]-player)==getPiece("pawn")):
		accum= getPawnMoves(position,playerSign,board,player)
	elif ((board[position]-player)==getPiece("knight")):
		accum= getKnightMoves(position,playerSign,board,player)
	elif ((board[position]-player)==getPiece("rook")):
		accum= getRookMoves(position,playerSign,board,player)
	elif ((board[position]-player)==getPiece("bishop")):
		accum= getBishopMoves(position,playerSign,board,player)
	elif ((board[position]-player)==getPiece("queen")):
		accum= getQueenMoves(position,playerSign,board,player)
	elif ((board[position]-player)==getPiece("king")):
		accum= getKingMoves(position,playerSign,board,player)

	#________________________CHECKING IF KING IS IN CHECK (REMOVED FOR TIME CONSTRAINTS)________________________
	# temp=[]
	# if(shouldCheck):
	# 	#temp=list(accum)
	# 	tempBoard=list(board)
	# 	for n in (GetPlayerPositions(board,player)):
	# 		if (board[n]-player==5):
	# 			if (IsPositionUnderThreat(board,n,player)):
	# 				#print("hi")
	# 				for i in accum:
	# 					tempBoard[i]=tempBoard[position]
	# 					tempBoard[position]=0
	# 					if (IsPositionUnderThreat(tempBoard,n,player)==True):
	# 						tempBoard=list(board)
	# 						removeFromList(accum,i)
	# 			break

	return accum

def IsPositionUnderThreat (board,position,player):
	accum=[]
	if (player==10):
		enemy=20
	else:
		enemy=10
	for i in range(0,64,1):
		if (getPlayer(board,i)==enemy):
			accum=accum+GetPieceLegalMoves(board,i)
	for n in range(0, len(accum), 1):
		if (accum[n] == position):
			return True
	return False
	
def getPlayer (board,position):
	if (board[position]>=10 and board[position]<20):
		return 10
	elif (board[position]>=20):
		return 20
	else:
		return 0



def basicAI(board,player):
	accum=[]
	piece=[]
	L1=GetPlayerPositions(board,player)
	for n in L1:
		print (GetPieceLegalMoves(board,n))
		for i in (GetPieceLegalMoves(board,n)):
			print(IsPositionUnderThreat(board,i,player))
			if (IsPositionUnderThreat(board,i,player)==False):
				piece=piece+[n]
				accum=accum+[i]
	print("ADSA")
	print (piece)
	print(accum)
	return [piece[0],accum[0]]


def pieceValue(piece,player):
	value=0

	if (piece-player)==getPiece("pawn"):
		value=10
	elif (piece-player)==getPiece("knight"):
		value=30
	elif (piece-player)==getPiece("bishop"):
		value=30
	elif (piece-player)==getPiece("rook"):
		value=50
	elif (piece-player)==getPiece("queen"):
		value=90
	elif (piece-player)==getPiece("king"):
		value=900000
	return value

def mobility(board,player):
	count=0
	L1 = GetPlayerPositions(board, player)
	for n in L1:
		if (board[n]!=player+getPiece("pawn")):
			count += len((GetPieceLegalMoves(board, n)))
	return count

#num white pieces vs num black pieces
def difference(board,player,piece,enemy,positionsWhite,positionsBlack):
	val=numPieces(board,player,getPiece(piece),positionsWhite)-numPieces(board,enemy,getPiece(piece),positionsBlack)
	return val

def numPieces(board,player,piece,positions):
	count=0
	for n in positions:
		if (board[n]-player==piece):
			count=count+1
	return count

#return the value of a board state for white and make sure king has highest value
def evalFunction(board):
	player=10
	enemy=20
	positionsWhite=GetPlayerPositions(board, player)
	positionsBlack=GetPlayerPositions(board, enemy)
	#num pieces
	listPieces = ["king","queen","rook","bishop","knight","pawn"]
	listWeights = [200,9,5,3,3,1]
	f=0
	for i in range (len(listPieces)):
		f+=listWeights[i]*difference(board,player,listPieces[i],enemy,positionsWhite,positionsBlack)

	#mobility
	f=f+0.1*(mobility(board,player)-mobility(board,enemy))

	return (float(f))


#returns a list of tuples, (position,possible new position), of all actions for given player
def allMoves (board,player):
	accum=[]
	L1 = GetPlayerPositions(board, player)
	for n in L1:
		for i in (GetPieceLegalMoves(board, n)):
			accum.append((n,i))
	return accum


def getNewBoard (board,action):
	newBoard=list(board)
	newBoard[action[1]]=newBoard[action[0]]
	newBoard[action[0]]=0
	return newBoard

def  Get_LeveLOrder(evalTree):
	x=queue()
	x.enqueue(evalTree)
	accum=[]
	while (x.isEmpty()==False):
		y=x.dequeue()
		v=y[1]
		accum=accum+[v[0]]
		for i in range(1,len(v)):
			x.enqueue(v[i])
	return accum

#return best action, best value, candidate moves
def minmax (board, player, remainingTime, depth=0, alpha=-1.0*float('inf'), beta=float('inf')):
	DEPTH_LIMIT=3
	start_time = time.time()

	#if at depth limit, return an abritrary move, value returned by evaluation function for that state, and arbitrary candidate moves
	if (depth == DEPTH_LIMIT or remainingTime<=0):
		evalTree=evalFunction(board)
		return False,None,None,[evalTree],evalTree

	evalTree = []
	move=[]
	candidateMoves=[]
	actions=allMoves(board,player)
	for i in range(len(actions)):
		newBoard=getNewBoard(board,actions[i])
		if (player==10):  #if player is white
			result=minmax(newBoard,20,remainingTime-(time.time()-start_time),depth+1,alpha,beta)
			value=result[4]
			evalTree.append(result[3])
			if (depth==0):
				candidateMoves.append([actions[i],value])
			if (value > alpha):
				move=actions[i]
				alpha=value
				if (alpha>=beta):
					break
		elif (player==20):
			result=minmax(newBoard,10,remainingTime-(time.time()-start_time),depth + 1,alpha,beta)
			value=result[4]
			evalTree.append(result[3])
			if (depth==0):
				candidateMoves.append([actions[i], value])
			if (value < beta):
				move = actions[i]
				beta = value
				if (alpha>=beta):
					break

	if (depth == 0 and len(actions) == 0):
		status = False
	else:
		status = True
	if (player==10):
		fullTree=[alpha]+evalTree
		fullTree=[0]
		if (depth!=0):
			return status,move,candidateMoves,fullTree,alpha
		else:
			return status,move,candidateMoves,Get_LeveLOrder(fullTree),alpha
	elif (player==20):
		fullTree=[beta]+evalTree
		fullTree=[0]
		if (depth != 0):
			return status, move, candidateMoves, fullTree, beta
		else:
			return status, move, candidateMoves, Get_LeveLOrder(fullTree), beta

def chessPlayer(board,player):
	result=minmax(board,player,9.5)
	return [result[0],result[1],result[2],result[3]]

def getUserInput (board):
	done=False
	print(printBoard(board))
	while (done==False):
		while(True):
			count=0
			player2=20
			print ("Enter the piece you want to move: ")
			start=int(input())
			print ("Your possible moves for this piece are:")
			print (GetPieceLegalMoves(board, start))
			print ("Enter where you would like to move this piece: ")
			end=int(input())
			legalMoves=GetPieceLegalMoves(board,start)
			for n in range (0,len(legalMoves)):
				if (end==(legalMoves[n])):
					break
				count=count+1
			if (count==len(legalMoves)):
				print ("Invalid Input")
			else:
				board[end] = board[start]
				board[start] = 0
				print(printBoard(board))

				print("THINKING")
				startTime=time.time()
				#moveAI=basicAI(board,player2)
				result=chessPlayer(board,20)
				moveAI=result[1]
				print("FINISHED IN", time.time() - startTime, "s")
				#print(result[2])
				#print()
				#print(result[3])
				board[moveAI[1]]=board[moveAI[0]]
				board[moveAI[0]]=0
				print(printBoard(board))
				break


board=genBoard()
getUserInput (board)
