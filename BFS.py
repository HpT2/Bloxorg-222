def solve(block):
    passState = []
    Queue = []
    Queue.append(block)

    virtualStep = 0
    
    while Queue:
        current = Queue.pop(0)

        if not(current.isValidBlock()):
            continue

        if current in passState:
            continue
        
        passState.append(current)

        if current.isGoal():
            print("SUCCESS")
            print("COMSUME", virtualStep, "VIRTUAL STEP")
            return current

        if current.rotation != "SPLIT":
            virtualStep += 4
            
            Queue.append(current.UP())
            Queue.append(current.RIGHT())
            Queue.append(current.DOWN())
            Queue.append(current.LEFT())
        else: 
            virtualStep += 8

            Queue.append(current.SPLIT_LEFT())
            Queue.append(current.SPLIT_RIGHT())
            Queue.append(current.SPLIT_UP())
            Queue.append(current.SPLIT_DOWN())
            
            Queue.append(current.SPLIT_LEFT_1())
            Queue.append(current.SPLIT_RIGHT_1())
            Queue.append(current.SPLIT_UP_1())
            Queue.append(current.SPLIT_DOWN_1())
