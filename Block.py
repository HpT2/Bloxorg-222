import copy
import switch_handle
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
		
	
	def isvalidBlock(self):
		if isFloor(self):
			x = self.x
			y = self.y
			rotation = self.rotation
			board = self.board
			x1= self.x1
			y1= self.y1
        	# Case: Gach yeu
			if rotation == "STANDING" and board[y][x] == 2: return False
        
			# Case: chu X (Heavy swich) -> T, C, O
			elif rotation == "STANDING" and board[y][x] == 3: return switch_handle.isNumberThree(self,x,y)
        
			# Case: chu O (Light swich) -> only close
			elif board[y][x] == 4: return switch_handle.isNumberFour(self,x,y)
			elif rotation == "LAYING_X" and board[y][x+1] == 4: return switch_handle.isNumberFour(self,x+1,y)
			elif rotation == "LAYING_Y" and board[y+1][x] == 4: return switch_handle.isNumberFour(self,x,y+1)
			elif rotation == "SPLIT" and board[y1][x1] == 4: return switch_handle.isNumberFour(self,x1,y1)
    
        	# Case: chu O (Light swich) -> T, C, O
			elif board[y][x] == 5: return switch_handle.isNumberFive(self,x,y)
			elif rotation == "LAYING_X" and board[y][x+1] == 5: return switch_handle.isNumberFive(self,x+1,y)
			elif rotation == "LAYING_Y" and board[y+1][x] == 5: return switch_handle.isNumberFive(self,x,y+1)
			elif rotation == "SPLIT" and board[y1][x1] == 5: return switch_handle.isNumberFive(self,x1,y1)
        
			# Case: chu O (Light swich) -> only open
			elif board[y][x] == 6: return switch_handle.isNumberSix(self,x,y)
			elif rotation == "LAYING_X" and board[y][x+1] == 6: return switch_handle.isNumberSix(self,x+1,y)
			elif rotation == "LAYING_Y" and board[y+1][x] == 6: return switch_handle.isNumberSix(self,x,y+1)
			elif rotation == "SPLIT" and board[y1][x1] == 6: return switch_handle.isNumberSix(self,x1,y1)
        
        	# Case: SPLIT -> phan ra thanh 2 khoi
			elif rotation == "STANDING" and board[y][x] == 7: return switch_handle.isNumberSeven(self,x,y)
			elif rotation == "SPLIT":
				if y==y1 and x==x+1: self.rotation = "LAYING_X"
				elif y==y1 and x==x-1: self.rotation = "LAYING_X"
				elif y==y1-1 and x==x1: self.rotation = "LAYING_Y"
				elif y==y1+1 and x==x1: self.rotation = "LAYING_Y"
        
        	# Case: chu X (Heavy swich) -> only open
			elif rotation == "STANDING" and board[y][x] == 8: return switch_handle.isNumberEight(self,x,y)
        
			else: return True
		else: return False

	def isFloor(block):
		x = block.x
		y = block.y
		rotation = block.rotation
		board = block.board
		if x>=0 and y>= 0 and x< MAP_COL and y< MAP_ROW and board[y][x] != 0:
			if rotation == "STANDING": return True
			elif rotation == "LAYING_Y":
				if y+1< MAP_ROW and board[y+1][x]!= 0: return True
				return False
			elif rotation == "LAYING_X":
				if x+1< MAP_COL and board[y][x+1]!= 0: return True
				return False
			else:
				x1= block.x1
				y1= block.y1
				if x1>=0 and y1>= 0 and x1< MAP_COL and y1 < MAP_ROW and board[y1][x1]!= 0:
					return True
				return False
		else: return False


	
	