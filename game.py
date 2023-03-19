import numpy as np
from Block import Block
import A_star
import BFS
import timeit
import os
import psutil
import argparse

def readMap(fileMap):
	with open(fileMap) as f:
		init_pos = [int(x) for x in f.readline().split(" ")] # read 1st line
		goal = [int(x) for x in f.readline().split(" ")] # read 2nd line
		num_of_switches = int(f.readline()) # read 3rd line
		switches = []
		for i in range(num_of_switches):
			switches.append(f.readline())
		return init_pos, goal, num_of_switches, switches

def main():
	args = argparse.ArgumentParser()
	args.add_argument("-stage", help="choose a stage")
	args.add_argument("-algorithm", help="BFS or A_star")
	args = args.parse_args()
	stage = "stage/stage"+args.stage+".txt"
	algorithm = args.algorithm

	init, goal, num_of_switches, switches = readMap(stage)
	map = np.loadtxt(stage,dtype=int,skiprows=3+num_of_switches)
	block = Block(init[1], init[0], "STANDING", None, map, switches=switches)

	print('Goal: {}'.format(goal))
	print("Init block: [{}, {}]".format(block.y, block.x))
	print("Map:\n{}".format(map))

	if algorithm == "BFS":
		print("##########Start solving with BFS algorithm##########")
		start = timeit.default_timer()
		finish_node = BFS.solve(block)
		stop = timeit.default_timer()
		print("Time taken BFS: " + str(round(stop - start, 4)) + " s")
		
		if(finish_node):
			path = []
			while(finish_node.parent):
				path = [finish_node.previousMove] + path
				finish_node = finish_node.parent
			print("Total step BFS: "+str(len(path)))
			print(path)
		else:
			print("FAILED")
	elif algorithm == "A_star":
		print("##########Start solving with A* algorithm##########")
		start = timeit.default_timer()
		finish_node = A_star.solve(block,goal)
		stop = timeit.default_timer()
		print("Time taken A*: " + str(round(stop - start, 4)) + " s")
		
		if(finish_node):
			last = finish_node
			path = []
			while(last.parent):
				path = [last.previousMove] + path
				last = last.parent
			print("Total step A*: "+str(len(path)))
			print(path)
		else:
			print("FAILED")
	else:
		print("Algorithm must be BFS or A-star")
	process = psutil.Process(os.getpid())
	print('Memory usage: ' + str(round(process.memory_info().rss / (1024 * 1024), 2)) + " MB")
process = psutil.Process(os.getpid())

if __name__ == "__main__":
	main()