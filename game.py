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

def printMap(map):
	for i in range(len(map)):
		for j in range(len(map[i])):
			if map[i][j] == 0:
				print(" ",end=" ")
				continue
			print(map[i][j],end=" ")
		print()

def main():
	args = argparse.ArgumentParser()
	args.add_argument("-stage", help="choose a stage")
	args.add_argument("-algorithm", help="BFS or A_star")
	args = args.parse_args()
	stage = "stage/stage"+args.stage+".txt"
	algorithm = args.algorithm
	path = []
	init, goal, num_of_switches, switches = readMap(stage)
	map = np.loadtxt(stage,dtype=int,skiprows=3+num_of_switches)
	block = Block(init[1], init[0], "STANDING", None, map, switches=switches)

	print('Goal: {}'.format(goal))
	print("Init block: [{}, {}]".format(block.y, block.x))
	print("Map:\n")
	printMap(map)

	if algorithm == "BFS":
		print("##########Start solving with BFS algorithm##########")
		start = timeit.default_timer()
		finish_node = BFS.solve(block)
		stop = timeit.default_timer()
		print("Time taken BFS: " + str(round(stop - start, 4)) + " s")
		
		if(finish_node):
			while(finish_node.parent):
				path = [finish_node.previousMove] + path
				finish_node = finish_node.parent
		else:
			print("FAILED")

	elif algorithm == "A_star":
		print("##########Start solving with A* algorithm##########")
		start = timeit.default_timer()
		finish_node = A_star.solve(block,goal)
		stop = timeit.default_timer()
		print("Time taken A*: " + str(round(stop - start, 4)) + " s")
		
		if(finish_node):
			while(finish_node.parent):
				path = [finish_node.previousMove] + path
				finish_node = finish_node.parent
		else:
			print("FAILED")
	else:
		print("Algorithm must be BFS or A-star")
	process = psutil.Process(os.getpid())
	print('Memory usage: ' + str(round(process.memory_info().rss / (1024 * 1024), 2)) + " MB")
	print("Total move: "+str(len(path)))
	print(path)

if __name__ == "__main__":
	main()