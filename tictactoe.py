cells = "         "
xTurn = True
inGame = True
matrix = [[cells[6], cells[3], cells[0]],
		  [cells[7], cells[4], cells[1]],
		  [cells[8], cells[5], cells[2]]]
print("---------")
print("|", matrix[0][2], matrix[1][2], matrix[2][2], "|")
print("|", matrix[0][1], matrix[1][1], matrix[2][1], "|")
print("|", matrix[0][0], matrix[1][0], matrix[2][0], "|")
print("---------")

while inGame:
	
	valid = False
	while not valid:
		coordinates = (str(input("Enter coordinates: "))).split()
		for num in coordinates:
			if not num.isnumeric():
				print("You should enter numbers!")
				valid = False
				break
			elif num not in ["1", "2", "3"]:
				print("Coordinates should be from 1 to 3!")
				valid = False
				break
			else:
				valid = True
		if valid:
			placeholder = matrix[int(coordinates[0]) - 1][int(coordinates[1]) - 1]
			if placeholder == " ":
				if xTurn:
					matrix[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = "X"
				else:
					matrix[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = "O"
				xTurn = not xTurn
					
				
			else:
				print("The cell is occupied! Choose another one!")
				valid = False
				

	print("---------")
	print("|", matrix[0][2], matrix[1][2], matrix[2][2], "|")
	print("|", matrix[0][1], matrix[1][1], matrix[2][1], "|")
	print("|", matrix[0][0], matrix[1][0], matrix[2][0], "|")
	print("---------")

	x_count, o_count = 0, 0
	for cell in cells:
		if cell == "X":
			x_count += 1
		if cell == "O":
			o_count += 1
	if abs(o_count - x_count) > 1:
		print("Impossible")
	else:
		
		x_win, o_win = False, False
		board = [[matrix[0][2], matrix[1][2], matrix[2][2]],
				[matrix[0][1], matrix[1][1], matrix[2][1]],
				[matrix[0][0], matrix[1][0], matrix[2][0]]]

				
		for row in board:
			if all(element == row[0] for element in row):
				if(row[0] == "O"):
					o_win = True
				elif(row[0] == "X"):
					x_win = True

		for i in range(0, 3):
			column = []
			for j in range(0, 3):
				column.append(board[j][i])
			if all(element == column[0] for element in column):
				if(column[0] == "O"):
					o_win = True
				elif(column[0] == "X"):
					x_win = True
			
		if (matrix[1][1] == matrix[2][2] and cells[2] == matrix[0][0]) or (matrix[1][1] == matrix[0][2] and matrix[0][2] == matrix[2][0]):
			if(matrix[1][1] == "O"):
				o_win = True
			elif(matrix[1][1] == "X"):
				x_win = True
			
		if x_win:
			print("X wins")
			inGame = False
		elif o_win:
			print("O wins")
			inGame = False
		
		if x_win == True and o_win == True:
			print("Impossible")
			inGame = False

		if o_win == False and x_win == False:
			if x_count + o_count == 9:
				print("Draw")
				inGame = False
			else:
				print("Game not finished")
			

