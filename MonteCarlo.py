import math
import random

def make_move(block):
	if block.rotation == "SPLIT":
		return [block.SPLIT_UP(), block.SPLIT_DOWN(),
	       		 block.SPLIT_LEFT(), block.SPLIT_RIGHT(),
				  block.SPLIT_UP_1(), block.SPLIT_DOWN_1(),
	       		   block.SPLIT_LEFT_1(), block.SPLIT_RIGHT_1()]
	return [block.UP(), block.DOWN(),block.LEFT(), block.RIGHT()]

def createNode(root, depth):
	if root.block.isGoal() or not root.block.isValidBlock() or depth == 0:
		return root
	new_nodes = [Node(block, root) for block in make_move(root.block) if block.isValidBlock()]
	for node in new_nodes:
		node = createNode(node, depth-1)
		root.children.append(node)
	return root

class Node:
	def __init__(self, block, parent) -> None:
		self.block = block
		self.parent = parent
		self.children = []
		self.num_win = 0
		self.visits = 1

	def select(self):
		UCT_CONST = 1.414 # adjust to balance exploration and exploitation
		best_child = None
		best_score = float('-inf')
		for child in self.children:
			score = child.num_win / child.visits + UCT_CONST * math.sqrt(
			math.log(self.visits) / child.visits)
			#score = child.num_win / child.visits
			
			if score >= best_score and child.block.isValidBlock():
				best_child = child
				best_score = score
		#print(best_child.block.previousMove)
		#print(best_child.visits)
		#print(best_score)
		return best_child

	def simulate(self):
		block = self.block
		node = self
		while block.isValidBlock():
			if block.isGoal():
				return 1
			if len(node.children) == 0:
				return 0
			node = random.choice(node.children)
			block = node.block
		return 0
	
	def backpropergate(self, win):
		"""
        Backpropagates the score of a simulated game to all ancestor nodes.
		"""
		node = self
		while node is not None:
			node.visits += 1
			node.num_win += win
			node = node.parent
		
def MonteCarlo(node, max_ite):
	
	for i in range(max_ite):
		exam_node = node

		while exam_node.children:
			exam_node = exam_node.select()
		
		if exam_node.block.isValidBlock():
			exam_node = createNode(exam_node, 1)
		
		win = exam_node.simulate()

		exam_node.backpropergate(win)
	if len(node.children) == 0:
		return node
	score = 0
	for child in node.children:
		if child.num_win / child.visits > score:
			score = child.num_win / child.visits
			best = child
	if score == 0:
		best = random.choice(node.children)
	return best
	best_child = max(node.children, key= lambda child:  child.visits)
	print(best_child.visits)
	return max(node.children, key= lambda child: child.num_win / child.visits)


def solve(block):
	root = Node(block, None)
	node = root
	i = 0
	while not root.block.isGoal() and i < 20:
		node = MonteCarlo(node, 10)
		i+=1
		#print(node.block.previousMove, i)
	return node.block