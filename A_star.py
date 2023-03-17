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
	path = []

	solver = A_star(h_func, g_func)

	if (solver.createNode(block,stage.goal).value == 0):
		return examine
	move = getMove(block)
	open = [solver.createNode(x,stage.goal) for x in move]
	open.sort(key = lambda x: x.value, reverse=True)

	while(len(open) > 0):
		exam_node = [open.pop()] + exam_node 

		x = exam_node.pop(0)
		value = x.value


		if (stage.GameOver(x.block)):
			continue
		
		if (x.block in close):
			continue

		if(value == 0 ):
			print("done")
			return path
			break

		#print("Move: {}".format(x.block.previousMove + " Cur: [{},{}][{},{}]".format(x.block.pos1.y,x.block.pos1.x,x.block.pos2.y,x.block.pos2.x)) + " Dead: {}".format(str(stage.GameOver(x.block))))
		close.append(x.block)
		path.append(x.block)

		move = getMove(x.block)
		new_nodes = [solver.createNode(y,stage.goal) for y in move]
		new_nodes.sort(key = lambda x: x.value, reverse=True)
		for node in new_nodes:
			open.append(node)
	print("Failed")
	return exam_node
	

def h_func(block,goal):
	return (math.dist([block.pos1.y, block.pos1.x], goal) + math.dist([block.pos2.y, block.pos2.x], goal)) / 2

def g_func(x):
	return x 

class Node:
	def __init__(self, h, g, block, goal ) -> None:
		self.value = h(block,goal ) + g(0)
		self.block = block

class A_star:
	def __init__(self, h, g) -> None:
		self.h_func = h
		self.g_func = g

	def createNode(self,block,goal) -> Node :
		return Node(self.h_func, self.g_func, block,goal)
	

