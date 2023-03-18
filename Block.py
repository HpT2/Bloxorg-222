import copy

class Block:
	def __init__(self, x, y, rotation, parent, board, x1=None,y1=None):
		self.x = x
		self.y = y
		self.rotation = rotation
		self.parent = parent
		self.board = copy.deepcopy(board)
		self.x1 = x1
		self.y1 = y1

	def UP(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board)
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
		newBlock = Block(self.x, self.y, self.rotation, self, self.board)
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
		newBlock = Block(self.x, self.y, self.rotation, self, self.board)
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
		newBlock = Block(self.x, self.y, self.rotation, self, self.board)
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
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, self.x1, self.y1)
		newBlock.y -= 1
		return newBlock
	
	def SPLIT_DOWN(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, self.x1, self.y1)
		newBlock.y += 1
		return newBlock
	
	def SPLIT_LEFT(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, self.x1, self.y1)
		newBlock.x -= 1
		return newBlock
	
	def SPLIT_RIGHT(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, self.x1, self.y1)
		newBlock.x += 1
		return newBlock
	
	def SPLIT_UP_1(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, self.x1, self.y1)
		newBlock.y1 -= 1
		return newBlock
	
	def SPLIT_DOWN_1(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, self.x1, self.y1)
		newBlock.y1 += 1
		return newBlock
	
	def SPLIT_LEFT_1(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, self.x1, self.y1)
		newBlock.x1 -= 1
		return newBlock
	
	def SPLIT_RIGHT_1(self):
		newBlock = Block(self.x, self.y, self.rotation, self, self.board, self.x1, self.y1)
		newBlock.x1 += 1
		return newBlock
	
	def isGoal(self):
		# statements
		if self.rotation == "STANDING" and self.board[self.y][self.x] == 9:
			return True
		else:
			return False