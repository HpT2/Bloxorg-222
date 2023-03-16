def solve(stage, block):
	if(stage.goal == [block.pos1.y,block.pos1.x] and stage.goal == [block.pos2.y,block.pos2.x]):
		print("Done")