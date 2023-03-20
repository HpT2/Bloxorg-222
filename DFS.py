def solve(block):
    Stack = []
    Stack.append(block)

    passState = []
    passState.append(block)

    virtualStep = 0

    while Stack:
        curr = Stack.pop()
        
        if curr.isGoal():
            print("SUCCESS")
            print("COMSUME", virtualStep, "VIRTUAL STEP")
            return curr

        if curr.rotation != 'SPLIT':
            virtualStep += 4

            move(Stack, curr.UP(), passState)
            move(Stack, curr.RIGHT(), passState)
            move(Stack, curr.DOWN(), passState)
            move(Stack, curr.LEFT(), passState)
        else:
            virtualStep += 8

            move(Stack, curr.SPLIT_LEFT(), passState)
            move(Stack, curr.SPLIT_RIGHT(), passState)
            move(Stack, curr.SPLIT_UP(), passState)
            move(Stack, curr.SPLIT_DOWN(), passState)
            
            move(Stack, curr.SPLIT_LEFT_1(), passState)
            move(Stack, curr.SPLIT_RIGHT_1(), passState)
            move(Stack, curr.SPLIT_UP_1(), passState)
            move(Stack, curr.SPLIT_DOWN_1(), passState)
    return False

def move(Stack, block, passState):
    if block.isValidBlock():
        if isVisited(block, passState):
            return None
        Stack.append(block)
        passState.append(block)
        return True 
    return False  

def isVisited(block, passState):
    if block.rotation == 'SPLIT':
        for item in passState:
            if (item.x  == block.x) and (item.y  == block.y) and (item.x1 == block.x1) and (item.y1 == block.y1) and (item.rotation == block.rotation) and (item.board == block.board).all():
                return True
    else:
        for item in passState:
            if (item.x == block.x) and (item.y == block.y) and (item.rotation == block.rotation) and (item.board == block.board).all():
                return True
    return False
