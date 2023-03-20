import numpy as np
import time
import os
import psutil
import sys
from Block import Block
import A_star, BFS, DFS

def readMap(fileMap):
	with open(fileMap) as f:
		init_pos = [int(x) for x in f.readline().split(' ')]		# read 1st line
		goal = [int(x) for x in f.readline().split(' ')]			# read 2nd line
		num_of_switches = int(f.readline())							# read 3rd line
		switches = []
		for i in range(num_of_switches):
			switches.append(f.readline())
		return init_pos, goal, num_of_switches, switches

def main():
	# Argument from command line
	stage = 'stage/stage' + sys.argv[1] + '.txt'
	algorithm = sys.argv[2]

	# Initialization
	init, goal, num_of_switches, switches = readMap(stage)
	map = np.loadtxt(stage, dtype = int, skiprows = 3 + num_of_switches)
	block = Block(init[1], init[0], 'STANDING', None, map, switches = switches)

	# Print
	print('Goal: {}'.format(goal))
	print('Init: [{}, {}]'.format(block.y, block.x))
	print('Map:\n{}'.format(map))
	print('\n[========== Solve with ' + algorithm.upper() + ' algorithm ==========]')

	# Time completion
	start_time = time.time()

	if (algorithm.lower() == 'dfs'):
		finish_node = DFS.solve(block)
	elif (algorithm.lower() == 'bfs'):
		finish_node = BFS.solve(block)
	elif (algorithm.lower() == 'a-star'):
		finish_node = A_star.solve(block, goal)
	else:
		print('There is no suitable algorithm! You can try bfs, dfs, a-star algorithms.')
		exit()
	
	print('Time taken: ' + str(round(time.time() - start_time, 4)) + ' seconds')

	# Step and path to destination
	if (finish_node):
		path = []
		while (finish_node.parent):
			path = [finish_node.previousMove] + path
			finish_node = finish_node.parent
		print('Total step: ' + str(len(path)))
		print(path)
	else:
		print('FAILED!')
	
	# Processing Memory
	process = psutil.Process(os.getpid())
	print('Memory usage: ' + str(round(process.memory_info().rss / (1024 * 1024), 2)) + ' MB')

process = psutil.Process(os.getpid())

if __name__ == "__main__":
	# python3 run.py <stage> <algorithm>
	main()
