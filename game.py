from Stage import Stage
import numpy as np
from Block import Block
import A_star

"""input lấy theo màn 3, dòng 1 là vị trí khởi đầu, dòng 2 là goal"""
with open("stage1.txt") as file:
	init = [int(x) for x in file.readline().split(' ')]
	goal = [int(x) for x in file.readline().split(' ')]


map = np.loadtxt("Stage1.txt",dtype=int,skiprows=2)
stage = Stage(map,goal)

"""do numpy array đọc theo y trước x nên tọa độ phải theo thứ tự (y,x)"""
pos1 = [init[1],init[0]] 
pos2 = [init[3],init[2]]
block = Block(pos1,pos2)

print('Goal: {}'.format(stage.goal))
print("block: [{},{}] [{},{}]".format(block.pos1.y, block.pos1.x, block.pos2.y, block.pos2.x))
print("Map:\n{}".format(stage.map))
"""Test"""
block.RIGHT()
block.UP()
block.RIGHT()
block.RIGHT()
block.RIGHT()
block.UP()
block.LEFT()
block.DOWN()
block.RIGHT()
block.UP()
block.UP()
block.RIGHT()
block.RIGHT()
block.RIGHT()
block.DOWN()
block.LEFT()
block.DOWN()
block.RIGHT()	
block.DOWN()
block.RIGHT()
block.UP()
block.LEFT()
block.LEFT()
block.DOWN()
block.RIGHT()
block.UP()
block.UP()
block.LEFT()
block.DOWN()
block.RIGHT()
block.UP()
block.LEFT()
block.DOWN()
block.RIGHT()
A_star.solve(stage,block)
