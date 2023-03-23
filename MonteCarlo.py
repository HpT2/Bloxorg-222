import math
import random

def make_move(block):
	if block.rotation == "SPLIT":
		return [block.SPLIT_UP(), block.SPLIT_DOWN(),
	       		 block.SPLIT_LEFT(), block.SPLIT_RIGHT(),
				  block.SPLIT_UP_1(), block.SPLIT_DOWN_1(),
	       		   block.SPLIT_LEFT_1(), block.SPLIT_RIGHT_1()]
	return [block.UP(), block.DOWN(),block.LEFT(), block.RIGHT()]

def h(block ,goal):
		if block.rotation != "SPLIT":
			return (math.dist([block.y, block.x],goal))
		return ((math.dist([block.y, block.x],goal)) + math.dist([block.y, block.x],goal)) / 2
	

def createNode(root, goal):
	new_nodes = [Node(block, root, goal) for block in make_move(root.block) if block.isValidBlock()]
	for node in new_nodes:
		root.children.append(node)
	return root

def examined(node):
	examined = []
	while node.parent:
		node = node.parent
		examined.append(node.block)
	return examined

class Node:
	def __init__(self, block, parent, goal) -> None:
		self.block = block
		self.parent = parent
		self.children = []
		self.score = -h(block, goal)
		self.visits = 1

	def select(self):
		if self.children == []:
			return self
		UCT_CONST = 1.414 # adjust to balance exploration and exploitation
		best_child = None
		best_score = float('-inf')
		for child in self.children:
			score = child.score / child.visits + UCT_CONST * math.sqrt(
			math.log(self.visits) / child.visits)
			#score = child.score / child.visits
			
			if score > best_score:
				best_child = child
				best_score = score
		if best_child.block in examined(best_child):
			self.children.remove(best_child)
			return self.select()
		return best_child

	def simulate(self):
		if not self.children:
			return self.score
		node = random.choice(self.children) 
		return node.score
	
	def backpropergate(self, score):
		"""
        Backpropagates the score of a simulated game to all ancestor nodes.
		"""
		node = self
		while node is not None:
			node.visits += 1
			node.score += score
			node = node.parent
		
def MonteCarlo(node, max_ite, goal):
	
	for i in range(max_ite):
		exam_node = node

		while exam_node.children:
			exam_node = exam_node.select()
		
		exam_node = createNode(exam_node, goal)
		
		score = exam_node.simulate()	

		exam_node.backpropergate(score)

	return max(node.children, key= lambda child: child.visits)


def solve(block, goal):
	root = Node(block, None, goal)
	node = root
	while not node.block.isGoal():
		node = MonteCarlo(node, 100, goal)
	return node.block