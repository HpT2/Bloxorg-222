import copy

class Block:
	def __init__(self, x, y, rotation, parent, board, previousMove= None, x1=None,y1=None):
		self.x = x
		self.y = y
		self.rotation = rotation
		self.parent = parent
		self.board = copy.deepcopy(board)
		self.previousMove = previousMove
		self.x1 = x1
		self.y1 = y1

	def UP(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, "UP")
		if self.rotation == "STANDING":
			newBlock.y -= 2
			newBlock.rotation = "LAYING_Y"
		elif newBlock.rotation == "LAYING_X":
			newBlock.y -= 1
		elif newBlock.rotation == "LAYING_Y":
			newBlock.y -= 1
			newBlock.rotation = "STANDING"
		return newBlock
	
	def DOWN(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board,"DOWN")
		if newBlock.rotation == "STANDING":
			newBlock.y += 1
			newBlock.rotation = "LAYING_Y"
		elif newBlock.rotation == "LAYING_X":
			newBlock.y += 1
		elif newBlock.rotation == "LAYING_Y":
			newBlock.y += 2
			newBlock.rotation = "STANDING"
		return newBlock
	
	def LEFT(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, "LEFT")
		if newBlock.rotation == "STANDING":
			newBlock.x -= 2
			newBlock.rotation = "LAYING_X"
		elif newBlock.rotation == "LAYING_X":
			newBlock.x -= 1
			newBlock.rotation = "STANDING"
		elif newBlock.rotation == "LAYING_Y":
			newBlock.x -= 1
		return newBlock
	
	def RIGHT(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, "RIGHT")
		if newBlock.rotation == "STANDING":
			newBlock.x += 1
			newBlock.rotation = "LAYING_X"
		elif newBlock.rotation == "LAYING_X":
			newBlock.x += 2
			newBlock.rotation = "STANDING"
		elif newBlock.rotation == "LAYING_Y":
			newBlock.x += 1
		return newBlock
	
	def SPLIT_UP(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, "SPLIT 0 UP", self.x1, self.y1)
		newBlock.y -= 1
		return newBlock
	
	def SPLIT_DOWN(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, "SPLIT 0 DOWN", self.x1, self.y1)
		newBlock.y += 1
		return newBlock
	
	def SPLIT_LEFT(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, "SPLIT 0 LEFT", self.x1, self.y1)
		newBlock.x -= 1
		return newBlock
	
	def SPLIT_RIGHT(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, "SPLIT 0 RIGHT", self.x1, self.y1)
		newBlock.x += 1
		return newBlock
	
	def SPLIT_UP_1(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, "SPLIT 1 UP", self.x1, self.y1)
		newBlock.y1 -= 1
		return newBlock
	
	def SPLIT_DOWN_1(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, "SPLIT 1 DOWN", self.x1, self.y1)
		newBlock.y1 += 1
		return newBlock
	
	def SPLIT_LEFT_1(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, "SPLIT 1 LEFT", self.x1, self.y1)
		newBlock.x1 -= 1
		return newBlock
	
	def SPLIT_RIGHT_1(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, "SPLIT 1 RIGHT", self.x1, self.y1)
		newBlock.x1 += 1
		return newBlock
	
	def isGoal(self):
		# statements
		try:
			if self.rotation == "STANDING" and self.board[self.y][self.x] == 9:
				return True
			else:
				return False
		except:
			return False
		
	def GameOver(self):
		try:
			if self.rotation == "STANDING" and self.board[self.y][self.x] == 0 :
				return True
			if self.rotation == "LAYING_Y" and (self.board[self.y][self.x] == 0 or self.board[self.y+1][self.x] == 0 ):
				return True
			if self.rotation == "LAYING_X" and (self.board[self.y][self.x] == 0 or self.board[self.y][self.x+1] == 0 ):
				return True
			if self.rotation == "SPLIT" and self.board[self.y1][self.x1] == 0:
				return True
		except :
			return True
		return False
	
	def isSwitch(self):	
		pass