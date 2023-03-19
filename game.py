import numpy as np
from Block import Block
import A_star
import timeit
import os
import psutil

def readMap(fileMap):
	with open(fileMap) as f:
		init_pos = [int(x) for x in f.readline().split(" ")] # read 1st line
		goal = [int(x) for x in f.readline().split(" ")] # read 2nd line
		num_of_switches = int(f.readline()) # read 3rd line
		switches = []
		for i in range(num_of_switches):
			switches.append(f.readline())
		return init_pos, goal, num_of_switches, switches

"""input stage 1 là màn 1, stage2 là màn 2,... dòng 1 là vị trí khởi đầu, dòng 2 là goal. dòng 3 là số lượn switch
các dòng tiếp theo là switch, cuối cùng là map"""
init, goal, num_of_switches, switches = readMap("stage/stage8.txt")
map = np.loadtxt("stage/stage8.txt",dtype=int,skiprows=3+num_of_switches)

"""do numpy array đọc theo y trước x nên tọa độ phải theo thứ tự (y,x)""" 

block = Block(init[1], init[0], "STANDING", None, map, switches=switches)


print('Goal: {}'.format(goal))
print("block: [{}, {}]".format(block.y, block.x))
print("Map:\n{}".format(map))

"""Test"""
print("##########Start solving with A* algorithm##########")
start = timeit.default_timer()

finish_node = A_star.solve(block, goal)
stop = timeit.default_timer()


print("Time taken: " + str(round(stop - start, 4)) + " s")

process = psutil.Process(os.getpid())

print('Memory usage: ' + str(round(process.memory_info().rss / (1024 * 1024), 2)) + " MB")
if(finish_node):
	last = finish_node
	path = []
	while(last.parent):
		path = [last.previousMove] + path
		last = last.parent
	print("Total step: "+str(len(path)))
	print(path)
else:
	print("FAILED")