import math
from queue import PriorityQueue


class Node:
	def __init__(self,block, goal, parent= None):
		self.block = block
		self.parent = parent
		self.h_val = self.h(goal)
		self.g_val = self.g(parent)
		self.f_val = self.g_val + self.h_val

	def h(self ,goal):
		return ((math.dist([self.block.y,self.block.x],goal) + (( math.dist([self.block.y1,self.block.x1],goal)) if self.block.y1 else 0 )))/2
	
	def g(self, parent):
		if parent == None:
			return 0
		return parent.g_val + 1
	
	def __lt__(self, other) -> bool:
		return self.f_val < other.f_val

	def __eq__(self, __o: object) -> bool:
		if __o:
			return self.f_val == __o.f_val and self.block.x == __o.block.x \
				and self.block.y == __o.block.y and self.block.x1 == __o.block.x1 \
					and self.block.y1 == __o.block.y1 and (self.block.board == __o.block.board).all() \
						and self.block.rotation == __o.block.rotation
		return False
	

def solve(block,goal):
	root = Node(block,goal)
	queue = PriorityQueue()
	queue.put(root)
	close = []

	while not(queue.empty()):
		exam_node = queue.get()
		exam_block = exam_node.block

		if exam_block.isGoal():
			return exam_block

		if not(exam_block.isValidBlock()):
			continue

		if exam_node in close:
			continue

		close.append(exam_node)

		newBlocks = [exam_block.UP(), exam_block.DOWN(), exam_block.LEFT(), exam_block.RIGHT()]
		if exam_block.rotation == "SPLIT":
			newBlocks += [exam_block.SPLIT_UP(), exam_block.SPLIT_DOWN(),
	       				exam_block.SPLIT_LEFT(), exam_block.SPLIT_RIGHT(),
						 exam_block.SPLIT_UP_1(), exam_block.SPLIT_DOWN_1(),
	       				  exam_block.SPLIT_LEFT_1(), exam_block.SPLIT_RIGHT_1()]
		
		new_nodes = [Node(newBlock, goal, exam_node) for newBlock in newBlocks]

		for node in new_nodes:
			queue.put(node)

		



    	

