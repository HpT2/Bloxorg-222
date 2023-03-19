import numpy as np
from Block import Block
import A_star
import timeit
import os
import psutil

"""input stage 1 là màn 1, stage2 là màn 3, dòng 1 là vị trí khởi đầu, dòng 2 là goal"""
with open("stage/stage6.txt") as file:
	init = [int(x) for x in file.readline().split(' ')]
	goal = [int(x) for x in file.readline().split(' ')]


map = np.loadtxt("stage/stage6.txt",dtype=int,skiprows=2)

"""do numpy array đọc theo y trước x nên tọa độ phải theo thứ tự (y,x)""" 
block = Block(init[1], init[0], "STANDING", None, map)


print('Goal: {}'.format(goal))
print("block: [{}, {}]".format(block.y, block.x))
print("Map:\n{}".format(map))

"""Test"""
start = timeit.default_timer()
finish_node = A_star.solve(block, goal)
stop = timeit.default_timer()

print("A-star take: " + str(round(stop - start, 4)) + " s")

process = psutil.Process(os.getpid())

print('Memory usage: ' + str(round(process.memory_info().rss / (1024 * 1024), 2)) + " MB")
if(finish_node):
	last = finish_node
	path = []
	while(last.parent):
		path = [last.previousMove] + path
		#print('[{} {}] [{} {}] {}'.format(last.block.pos1.y,last.block.pos1.x,last.block.pos2.y, last.block.pos2.x,last.block.previousMove))
		last = last.parent
	print(len(path))
	print(path)
else:
	print("FAILED")