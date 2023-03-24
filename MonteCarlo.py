import math
import random

def make_move(block):
	if block.rotation == "SPLIT":
		return [block.SPLIT_UP(), block.SPLIT_DOWN(),
	       		 block.SPLIT_LEFT(), block.SPLIT_RIGHT(),
				  block.SPLIT_UP_1(), block.SPLIT_DOWN_1(),
	       		   block.SPLIT_LEFT_1(), block.SPLIT_RIGHT_1()]
	return [block.UP(), block.DOWN(),block.LEFT(), block.RIGHT()]



class Node:
	def __init__(self, block, parent) -> None:
		self.block = block
		self.parent = parent
		self.children = []
		self.score = 0
		self.visits = 1


	def select(self):
		if not self.children == []:
			best_child = None
			score = float('-inf')
			c = math.sqrt(2)
			for child in self.children:
				new_score = child.score / child.visits + c * math.sqrt(math.log(self.visits) / child.visits)
				if score < new_score :
					score = new_score
					best_child = child
				return best_child
		


		
	def expand(self):
		self.children = [Node(block, self) for block in make_move(self.block)]


	def simulate(self):
		block = self.block
		while not block.isGoal():
			if not block.isValidBlock():
				return  -1
			move = [block for block in make_move(self.block)]
			block = random.choice(move)
			#print(block.previousMove)
		return 1

	
	def backpropagate(self, score):
		node = self
		while node is not None:
			node.visits += 1
			node.score += score
			node = node.parent


	
def MonteCarlo(root, max_ite):
	for i in range(max_ite):
		node = root

		#selection
		i = 0
		while not node.children == []:
			node = node.select()
			i += 1
			#print(i)


			
		#expansion
		if not node.children and not node.block.isGoal():
			node.expand()
		

		#simulation
		score = node.simulate()

		#backpropagation
		node.backpropagate(score)
		
	return min(root.children, key=lambda child:  child.visits)

def solve(block,goal):
	root = Node(block, None)
	node = root
	while not node.block.isGoal():
		node = MonteCarlo(node, 10)

		print(node.block.previousMove, node.score)
	return node.block