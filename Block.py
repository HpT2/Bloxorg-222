class Block:
	"""Đối tượng Block biểu diễn cho khối, có 2 vị trí kề nhau là pos1 và pos2, mỗi vị trí có tọa độ (y,x)"""
	def __init__(self, pos1, pos2, previousMove = None) -> None:
		self.pos1 = pos(pos1)
		self.pos2 = pos(pos2)
		self.previousMove = previousMove
	
	def UP(self):
		if self.pos1.x == self.pos2.x:
			if self.pos1.y == self.pos2.y or self.pos1.y < self.pos2.y:
				new_pos1_y = self.pos1.y - 1
				new_pos2_y = self.pos2.y - 2
			else:
				new_pos1_y = self.pos1.y - 2
				new_pos2_y = self.pos2.y - 1
		else:
			new_pos1_y = self.pos1.y - 1
			new_pos2_y = self.pos2.y - 1
		return Block([new_pos1_y, self.pos1.x], [new_pos2_y, self.pos2.x], "UP")

	def DOWN(self):
		if self.pos1.x == self.pos2.x:
			if self.pos1.y == self.pos2.y or self.pos1.y > self.pos2.y:
				new_pos1_y = self.pos1.y + 1
				new_pos2_y = self.pos2.y + 2
			else:
				new_pos1_y = self.pos1.y + 2
				new_pos2_y = self.pos2.y + 1
		else:
			new_pos1_y = self.pos1.y + 1
			new_pos2_y = self.pos2.y + 1
		return Block([new_pos1_y, self.pos1.x], [new_pos2_y, self.pos2.x], "DOWN")

	def RIGHT(self):
		if self.pos1.y == self.pos2.y:
			if self.pos1.x == self.pos2.x or self.pos1.x > self.pos2.x:
				new_pos1_x = self.pos1.x + 1
				new_pos2_x = self.pos2.x + 2
			else:
				new_pos1_x = self.pos1.x + 2
				new_pos2_x = self.pos2.x + 1
		else:
			new_pos1_x = self.pos1.x + 1
			new_pos2_x = self.pos2.x + 1
		return Block([self.pos1.y, new_pos1_x], [self.pos2.y, new_pos2_x], "RIGHT")
	
	def LEFT(self):
		if self.pos1.y == self.pos2.y:
			if self.pos1.x == self.pos2.x or self.pos1.x < self.pos2.x:
				new_pos1_x = self.pos1.x - 1
				new_pos2_x = self.pos2.x - 2
			else:
				new_pos1_x = self.pos1.x - 2
				new_pos2_x = self.pos2.x - 1
		else:
			new_pos1_x = self.pos1.x - 1
			new_pos2_x = self.pos2.x - 1
		return Block([self.pos1.y, new_pos1_x], [self.pos2.y, new_pos2_x], "LEFT")
	
	def __eq__(self, __o) -> bool:
		return self.pos1 == __o.pos1 and self.pos2 ==__o.pos2
			

class pos:
	def __init__(self,pos) -> None:
		self.y = pos[0]
		self.x = pos[1]

	def __eq__(self, __o: object) -> bool:
		return self.x == __o.x and self.y == __o.y