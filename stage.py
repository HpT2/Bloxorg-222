class Stage:
	"""Biểu diễn cho map của màn dưới dạng numpy array, 0 là dead, 1 là co thể đi vào"""
	def __init__(self, map, goal) -> None:
		self.map = map
		self.goal = goal

	def GameOver(self, block):
		try:
			if self.map[block.pos1.y][block.pos1.x] == 0 or self.map[block.pos2.y][block.pos2.x] == 0:
				return True
		except:
			return True
		return False

