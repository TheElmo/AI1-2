#setup board
# S R E G M I
# A T E N G N
# O U T A X I
# M I S T A N
# J T A R G I
# Q A R C E T

#Every letter on the board has a position consisting of a row and a col, f.e. the 's' in the top left has row=0,col=0. The 't' in the bottom right has row=5,col=5
board = [['s','r','e','g','m','i'],['a','t','e','n','g','n'],['o','u','t','a','x','i'],['m','i','s','t','a','n'],['j','t','a','r','g','i'],['q','a','r','c','e','t']]
x = len(board)
y = len(board[0])
#Words to find: Mist, Mis, Misten, Tang, Target, Taxi, Tart
words = ['mist','mis','misten','tang','target','taxi','tart']
#Define Solutions
#Here are the solutions for the 7 testwords on this board
sol = {'mist': [[3,0],[3,1],[3,2],[3,3]],
	   'misten': [[3,0],[3,1],[3,2],[2,2],[1,2],[1,3]],
	   'mis': [[0,4],[0,5],[0,0]],
	   'tang': [[1,1],[1,0],[1,5],[1,4]]}

#Print board
for row in board:
	row_string = ""
	for letter in row:
		row_string += letter + " "
	print(row_string)

#The program is tested on the board with the words, all the defined above. 
#But it can function on any board of any N*N size, if a word has multiple solutions (it exists multiple times) all solutions will be printen
def program(board, words):
	print("The board is ", x ," by ", y)

	for word in words:
		find(board, word)

def find(board, word):
	letter = word[0]
	for row in range(x):
		for col in range(y):
			#print(board[row][col])
			if(board[row][col] == letter):
				check_letter(row,col,word,1,[])

def check_letter(row,col,word,i,solut):
	solut.append([row,col])
	if len(word) == i:
		print("The solution for '" +word+ "' is: ",solut)
		#go back one step to try for more solutions
		del solut[-1]
		return True
	valid_ways = check_around([row,col],word[i])
	if len(valid_ways) == 0:
		#dead-end, remove choice from solution
		return False
	if len(valid_ways) != 0:
		i+=1
	for way in valid_ways:
		if check_letter(way[0],way[1],word,i,solut):
			return
		else:
			del solut[-1]

def check_around(position,check_for):
	valid_ways = []
	up = [val_num(position[0]-1,y), val_num(position[1],x)]
	down = [val_num(position[0]+1,y), val_num(position[1],x)]
	left = [val_num(position[0],y),val_num(position[1]-1,x)]
	right = [val_num(position[0],y),val_num(position[1]+1,x)]

	if board[left[0]][left[1]] == check_for:
		valid_ways.append([left[0],left[1]])

	if board[right[0]][right[1]] == check_for:
		valid_ways.append([right[0],right[1]])

	if board[up[0]][up[1]] == check_for:
		valid_ways.append([up[0],up[1]])

	if board[down[0]][down[1]] == check_for:
		valid_ways.append([down[0],down[1]])
	return valid_ways

def val_num(num,a):
	if num >= a:
		num = num - a
	if num < 0:
		num = num + a
	return num
program(board,words)


#CODE VAN DUO JELMER&WOUTER