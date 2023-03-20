def solve(block):
    passState = []
    Queue = []
    Queue.append(block)

    virtualStep = 0
    
    while Queue:
        current = Queue.pop(0)

        if current.isGoal():
            print("SUCCESS")
            print("COMSUME", virtualStep, "VIRTUAL STEP")
            return current

        if current.rotation != "SPLIT":
            virtualStep += 4

            move(Queue,current.UP(), passState)
            move(Queue,current.RIGHT(), passState)
            move(Queue,current.DOWN(), passState)
            move(Queue,current.LEFT(), passState)
        else: 
            virtualStep += 8

            move(Queue,current.SPLIT_LEFT(), passState)
            move(Queue,current.SPLIT_RIGHT(), passState)
            move(Queue,current.SPLIT_UP(), passState)
            move(Queue,current.SPLIT_DOWN(), passState)
            
            move(Queue,current.SPLIT_LEFT_1(), passState)
            move(Queue,current.SPLIT_RIGHT_1(), passState)
            move(Queue,current.SPLIT_UP_1(), passState)
            move(Queue,current.SPLIT_DOWN_1(), passState)
    return False

def move(Queue, block, passState):
    
    if block.isValidBlock():
        if isVisited(block,passState):
            return None

        Queue.append(block)
        passState.append(block)
        #print(flag)
        return True 

    return False  

def isVisited(block,passState):
    if block.rotation != "SPLIT":

        for item in passState:
            if (item.x == block.x) and (item.y == block.y) and (item.rotation == block.rotation) and (item.board == block.board).all():
                return True

    else: # case SPLIT
        for item in passState:
            if (item.x  == block.x) and (item.y  == block.y) and (item.x1 == block.x1) and (item.y1 == block.y1) and (item.rotation == block.rotation) and (item.board == block.board).all():
                return True

    return False