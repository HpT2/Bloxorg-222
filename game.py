from stage import Stage
import numpy as np
from Block import Block
import A_star
import timeit
import os
import psutil

"""input stage 1 là màn 1, stage2 là màn 3, dòng 1 là vị trí khởi đầu, dòng 2 là goal"""
with open("stage2.txt") as file:
	init = [int(x) for x in file.readline().split(' ')]
	goal = [int(x) for x in file.readline().split(' ')]


map = np.loadtxt("stage2.txt",dtype=int,skiprows=2)
stage = Stage(map,goal)

"""do numpy array đọc theo y trước x nên tọa độ phải theo thứ tự (y,x)"""
pos1 = [init[0],init[1]] 
pos2 = [init[2],init[3]]
block = Block(pos1,pos2)
block1 = Block(pos1,pos2)


print('Goal: {}'.format(stage.goal))
print("block: [{},{}] [{},{}]".format(block.pos1.y, block.pos1.x, block.pos2.y, block.pos2.x))
print("Map:\n{}".format(stage.map))

"""Test"""
start = timeit.default_timer()
finish_block = A_star.solve(stage,block)
stop = timeit.default_timer()

print("A-star take: " + str(round(stop - start, 4)) + " s")

process = psutil.Process(os.getpid())

print('Memory usage: ' + str(round(process.memory_info().rss / (1024 * 1024), 2)) + " MB")

last = finish_block
path = []
while(last.parent):
	path = [last.previousMove] + path
	last = last.parent
print(len(path))
print(path)
