import numpy as np
from Block import Block
import A_star
import BFS
import timeit
import os
import psutil
import argparse
import MonteCarlo
import pygame

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
		print("Time taken: " + str(round(stop - start, 4)) + " s")
		
		if(finish_node):
			while(finish_node.parent):
				path = [finish_node.previousMove] + path
				finish_node = finish_node.parent
		else:
			print("FAILED")

	elif algorithm == "Astar":
		print("##########Start solving with A* algorithm##########")
		start = timeit.default_timer()
		finish_node = A_star.solve(block,goal)
		stop = timeit.default_timer()
		print("Time taken: " + str(round(stop - start, 4)) + " s")
		
		if(finish_node):
			while(finish_node.parent):
				path = [finish_node.previousMove] + path
				finish_node = finish_node.parent
		else:
			print("FAILED")
	elif algorithm == "MonteCarlo":
		print("##########Start solving with Monte Carlo algorithm##########")
		start = timeit.default_timer()
		finish_node = MonteCarlo.solve(block)
		stop = timeit.default_timer()

		print("Time taken: " + str(round(stop - start, 4)) + " s")
		
		if(finish_node):
			while(finish_node.parent):
				path = [finish_node.previousMove] + path
				finish_node = finish_node.parent
		else:
			print("FAILED")
	else:
		print("Algorithm must be BFS or Astar or MonteCarlo")
	process = psutil.Process(os.getpid())
	print('Memory usage: ' + str(round(process.memory_info().rss / (1024 * 1024), 2)) + " MB")
	print("Total move: "+str(len(path)))
	print(path)

	'''init board'''
	BLACK = (0,0,0)
	global SCREEN, CLOCK, WINDOW_WIDTH, WINDOW_HEIGHT
	pygame.init()
	WINDOW_WIDTH = len(map[0]) * 40
	WINDOW_HEIGHT = len(map) * 40
	SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	CLOCK = pygame.time.Clock()
	SCREEN.fill(BLACK)
	while True:
		drawGrid(finish_node)
		drawBlock(finish_node)
		if not path:
			break
		finish_node = move(finish_node, path.pop(0))

		finish_node.isValidBlock()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			else:
				continue
		pygame.display.update()

def move(block, path):
	if path == "UP":
		return block.UP()
	if path == "DOWN":
		return block.DOWN()
	if path == "LEFT":
		return block.LEFT()
	if path == "RIGHT":
		return block.RIGHT()
	if path == "SPLIT 0 RIGHT":
		return block.SPLIT_RIGHT()
	if path == "SPLIT 0 LEFT":
		return block.SPLIT_LEFT()
	if path == "SPLIT 0 DOWN":
		return block.SPLIT_DOWN()
	if path == "SPLIT 0 UP":
		return block.SPLIT_UP()
	if path == "SPLIT 1 RIGHT":
		return block.SPLIT_RIGHT_1()
	if path == "SPLIT 1 LEFT":
		return block.SPLIT_LEFT_1()
	if path == "SPLIT 1 DOWN":
		return block.SPLIT_DOWN_1()
	if path == "SPLIT 1 UP":
		return block.SPLIT_UP_1()

def drawGrid(block):
	blockSize = 40 #Set the size of the grid block
	for x in range(0, WINDOW_WIDTH, blockSize):
		for y in range(0, WINDOW_HEIGHT, blockSize):
			rect = pygame.Rect(x, y, blockSize-5, blockSize-5)

			'''init board'''
			if block.board[int(y/40)][int(x/40)] == 1:
				pygame.draw.rect(SCREEN, (255,255,255), rect)

			if block.board[int(y/40)][int(x/40)] == 2:
				pygame.draw.rect(SCREEN, (255,255,0), rect)	

			if block.board[int(y/40)][int(x/40)] in [4,5,6]:
				pygame.draw.rect(SCREEN, (255,255,0), rect)
			'''draw block position'''
			
			if block.board[int(y/40)][int(x/40)] in [3,8]:
				pygame.draw.rect(SCREEN, (120,0,25), rect)

			if block.board[int(y/40)][int(x/40)] == 7:
				pygame.draw.rect(SCREEN, (120,250,125), rect)


def drawBlock(block):
	blockSize = 40 #Set the size of the grid block
	for x in range(0, WINDOW_WIDTH, blockSize):
		for y in range(0, WINDOW_HEIGHT, blockSize):
			rect = pygame.Rect(x, y, blockSize-5, blockSize-5)
			if x == block.x * 40 and y == block.y * 40:
				pygame.draw.rect(SCREEN, (255,0,0), rect)

			if block.rotation == "LAYING_X":
				if x == (block.x+1) * 40 and y == block.y * 40:
					pygame.draw.rect(SCREEN, (255,0,0), rect)

			if block.rotation == "LAYING_Y":
				if x == block.x * 40 and y == (block.y + 1) * 40:
					pygame.draw.rect(SCREEN, (255,0,0), rect)

			if block.rotation == "SPLIT":
				if x == block.x1 * 40 and y == block.y1 * 40:
					pygame.draw.rect(SCREEN, (255,0,0), rect)

	pygame.time.wait(1000)


if __name__ == "__main__":
	main()