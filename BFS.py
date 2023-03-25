def solve(block):
    passState = []
    Queue = []
    Queue.append(block)
    traversed = 0
    appended = 0
    
    while Queue:
        current = Queue.pop(0)
        traversed += 1
        
        if current.isGoal():
            print("SUCCESS")
            print("APPENDED", appended, "NODE")
            print("TRAVERSED", traversed, "NODE")
            return current

        if not(current.isValidBlock()):
            continue

        if current in passState:
            continue
        
        passState.append(current)

        if current.rotation != "SPLIT":
            appended += 4
            
            Queue.append(current.UP())
            Queue.append(current.RIGHT())
            Queue.append(current.DOWN())
            Queue.append(current.LEFT())
        else: 
            appended += 8

            Queue.append(current.SPLIT_LEFT())
            Queue.append(current.SPLIT_RIGHT())
            Queue.append(current.SPLIT_UP())
            Queue.append(current.SPLIT_DOWN())
            
            Queue.append(current.SPLIT_LEFT_1())
            Queue.append(current.SPLIT_RIGHT_1())
            Queue.append(current.SPLIT_UP_1())
            Queue.append(current.SPLIT_DOWN_1())
