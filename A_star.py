import math
from queue import PriorityQueue


class Node:
	def __init__(self,block, goal, parent= None):
		self.block = block
		self.parent = parent
		self.g_val = self.g(parent)
		self.f_val = self.g_val + self.h(goal)

	def h(self ,goal):
		if self.block.rotation != "SPLIT":
			return (math.dist([self.block.y,self.block.x],goal))
		return ((math.dist([self.block.y,self.block.x],goal)) + math.dist([self.block.y,self.block.x],goal)) / 2
	
	def g(self, parent):
		if parent == None:
			return 0
		return parent.g_val + 1
	
	def __lt__(self, other) -> bool:
		return self.f_val < other.f_val


	

def solve(block,goal):
	appended = 0
	root = Node(block,goal)
	queue = PriorityQueue()
	queue.put(root)
	close = []
	traversed = 0
	while not(queue.empty()):
		exam_node = queue.get()
		exam_block = exam_node.block
		traversed += 1
		if exam_block.isGoal():
			print("SUCCESS")
			print("APPENDED {} NODE".format(appended))
			print("TRAVERSED", traversed, "NODE")
			return exam_block

		if not(exam_block.isValidBlock()):
			continue

		if exam_block in close:
			continue

		close.append(exam_block)
		if exam_block.rotation != "SPLIT":
			newBlocks = [exam_block.UP(), exam_block.DOWN(), exam_block.LEFT(), exam_block.RIGHT()]
			appended += 4
		else:
			newBlocks = [exam_block.SPLIT_UP(), exam_block.SPLIT_DOWN(),
	       				exam_block.SPLIT_LEFT(), exam_block.SPLIT_RIGHT(),
						 exam_block.SPLIT_UP_1(), exam_block.SPLIT_DOWN_1(),
	       				  exam_block.SPLIT_LEFT_1(), exam_block.SPLIT_RIGHT_1()]
			appended += 8
		
		new_nodes = [Node(newBlock, goal, exam_node) for newBlock in newBlocks]

		for node in new_nodes:
			queue.put(node)

		



    	

