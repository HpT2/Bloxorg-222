class Block:
	"""Đối tượng Block biểu diễn cho khối, có 2 vị trí kề nhau là pos1 và pos2, mỗi vị trí có tọa độ (y,x)"""
	def __init__(self, pos1, pos2) -> None:
		self.pos1 = pos(pos1)
		self.pos2 = pos(pos2)
	
	def UP(self):
		if self.pos1.x == self.pos2.x:
			if self.pos1.y == self.pos2.y or self.pos1.y < self.pos2.y:
				self.pos1.y -= 1
				self.pos2.y -= 2
			else:
				self.pos1.y -= 2
				self.pos2.y -= 1
		else:
			self.pos1.y -= 1
			self.pos2.y -= 1

	def DOWN(self):
		if self.pos1.x == self.pos2.x:
			if self.pos1.y == self.pos2.y or self.pos1.y > self.pos2.y:
				self.pos1.y += 1
				self.pos2.y += 2
			else:
				self.pos1.y += 2
				self.pos2.y += 1
		else:
			self.pos1.y += 1
			self.pos2.y += 1

	def RIGHT(self):
		if self.pos1.y == self.pos2.y:
			if self.pos1.x == self.pos2.x or self.pos1.x > self.pos2.x:
				self.pos1.x += 1
				self.pos2.x += 2
			else:
				self.pos1.x += 2
				self.pos2.x += 1
		else:
			self.pos1.x += 1
			self.pos2.x += 1
	
	def LEFT(self):
		if self.pos1.y == self.pos2.y:
			if self.pos1.x == self.pos2.x or self.pos1.x < self.pos2.x:
				self.pos1.x -= 1
				self.pos2.x -= 2
			else:
				self.pos1.x -= 2
				self.pos2.x -= 1
		else:
			self.pos1.x -= 1
			self.pos2.x -= 1

			

class pos:
	def __init__(self,pos) -> None:
		self.x = pos[0]
		self.y = pos[1]