import math

def getMove(block):
	return [block.UP(),
			block.DOWN(),
			block.LEFT(),
			block.RIGHT()]

def solve(stage, block):
	open = []
	close = []
	exam_node = []

	solver = A_star(h_func, g_func)

	root = solver.createNode(block,stage)

	move = getMove(block)
	open = [solver.createNode(x,stage,root) for x in move]
	open.sort(key = lambda x: x.f, reverse=True)


	while(len(open) > 0):
		x = open.pop()

		if (stage.GameOver(x.block)):
			continue
		
		if (x.block in close):
			continue

		if(stage.finish(x.block)):
			print("Done")
			return x

		#print("Move: {}".format(x.block.previousMove + " Cur: [{},{}][{},{}]".format(x.block.pos1.y,x.block.pos1.x,x.block.pos2.y,x.block.pos2.x)) + " Dead: {}".format(str(stage.GameOver(x.block))))
		close.append(x.block)

		move = getMove(x.block)
		new_nodes = [solver.createNode(y,stage, x) for y in move]
		for node in new_nodes:
			open.append(node)
		open.sort(key = lambda x: x.f, reverse=True)
	print("Failed")
	return exam_node
	

def h_func(block,goal):
	return (math.dist([block.pos1.y, block.pos1.x], goal) + math.dist([block.pos2.y, block.pos2.x], goal)) / 2

def g_func(x):
	if(x):
		return x.g + 1
	return 1

class Node:
	def __init__(self, h, g, block, stage, parent ) -> None:
		self.h = h(block,stage.goal)
		self.g = g(parent)
		self.f = self.h + self.g
		self.block = block
		self.parent = parent

	def __eq__(self, __o: object) -> bool:
		if __o == None:
			return False
		return self.parent == __o.parent and self.block == __o.block

class A_star:
	def __init__(self, h, g) -> None:
		self.h_func = h
		self.g_func = g

	def createNode(self,block, stage, parent = None) -> Node :
		return Node(self.h_func, self.g_func, block, stage, parent)
	

