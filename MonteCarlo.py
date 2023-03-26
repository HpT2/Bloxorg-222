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
		self.children = [Node(block, self) for block in make_move(self.block) if block.isValidBlock()]

	def simulate(self):
		queue = []
		queue.append(self.block)
		close = []
		i = 0
		while queue:
			x = random.randint(0,len(queue)-1)
			current = queue.pop(x)
			#print(len(queue))
			if current.isGoal():
				while current:
					i += 1
					current = current.parent
				return -i*10

			if current in close:
				continue
			
			close.append(current)

			newBlocks = [block for block in make_move(current) if block.isValidBlock()]
			for block in newBlocks:
				queue.append(block)
	
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
		while node.children:
			node = node.select()
			#print(node.block.previousMove)


			
		#expansion
		if not node.children and not node.block.isGoal():
			node.expand()

		
		#print("Simulattion ",i)
		#simulation
		score = node.simulate()
		if score == None:
			node.score = float('-inf')
		#print(score)
		#backpropagation
		else:
			node.backpropagate(score)
		#print(score)
		#print(root.score)
	best = max(root.children, key=lambda child:  child.visits)
	return best

def solve(block):
	root = Node(block, None)
	node = root
	i = 0
	while not node.block.isGoal():
		node = MonteCarlo(node, 10+i)
		i = i+1


		#print(node.block.previousMove)
	return node.block