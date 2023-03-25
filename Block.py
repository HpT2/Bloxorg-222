import copy
from switch_handle import *

class Block:
	def __init__(self, x, y, rotation, parent, board, previousMove= None, x1=None,y1=None, switches = None):
		self.x = x
		self.y = y
		self.rotation = rotation
		self.parent = parent
		self.board = copy.deepcopy(board)
		self.previousMove = previousMove
		self.x1 = x1
		self.y1 = y1
		if switches == None:
			self.switches = parent.switches
		else:
			self.switches = switches

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
			if self.rotation == "STANDING" and self.board[self.y][self.x] == 6:
				return True
			else:
				return False
		except:
			return False
		
	def isValidBlock(self):
		try:
			# local definition
			x     = self.x
			y     = self.y
			x1    = self.x1
			y1    = self.y1
			rot   = self.rotation
			board = self.board

			if board[y][x] == 0:
				return False
			
			if rot == "STANDING" and board[y][x] == 2:
				return False 
			if rot == "LAYING_Y" and board[y+1][x] == 0:
				return False
			if rot == "LAYING_X" and board[y][x+1] == 0:
				return False
			if rot == "SPLIT" and board[y1][x1] == 0:
				return False

			# Case 3: Chữ X
			if rot == "STANDING" and board[y][x] == 3:
				isNumberThree(self,y,x)

			# Case 4: Cục tròn đặc .
			if board[y][x] == 4:
				isNumberFour(self,y,x)
			if rot == "LAYING_X" and board[y][x+1] == 4:
				isNumberFour(self,y,x+1)
			if rot == "LAYING_Y" and board[y+1][x] == 4:
				isNumberFour(self,y+1,x)
			if rot == "SPLIT" and board[y1][x1] == 4:
				isNumberFour(self,y1,x1)


			# Case 5: Phân thân 
			if rot == "STANDING" and board[y][x] == 5:
				isNumberFive(self,y,x)
			# Case7_1: MERGE BLOCK
			if rot == "SPLIT": # check IS_MERGE
				# case LAYING_X: x first
				if y == y1 and x == x1 -1:
					self.rotation = "LAYING_X"

				# case LAYING_X: x1 first
				if y == y1 and x == x1 + 1:
					self.rotation = "LAYING_X"
					self.x   = x1

				# case LAYING_Y: y first
				if x == x1 and y == y1 - 1:
					self.rotation = "LAYING_Y"
				
				# case LAYING_Y: y1 first
				if x == x1 and y == y1 + 1:
					self.rotation = "LAYING_Y"
					self.y   = y1
			return True
		except:
			return False

	def __eq__(self, __o: object) -> bool:
		if __o:
			if self.rotation == "SPLIT":
				return self.x == __o.x \
					and self.y == __o.y and self.x1 == __o.x1 \
						and self.y1 == __o.y1 and (self.board == __o.board).all()\
						 and self.rotation == __o.rotation
			else:
				return self.x == __o.x and self.y == __o.y \
					and self.rotation == __o.rotation and (self.board == __o.board).all()
		return False
