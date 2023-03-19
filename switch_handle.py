# Case: chu X (Heavy swich) -> T, C, O
def isNumberThree(block,x,y):
    # format: x y numToggle <a,b>*numToggle numClose <a,b>*numClose numOpen <a,b>*numOpen
    board = block.board
    for item in manaboard:
        if x==item[0] and y==item[1]:
            numToggle = item[2]
            index=2
            for i in range(numToggle):
                a = item[2*i+3]
                b = item[2*i+4]
                if board[b][a]==0: board[b][a]=1
                elif board[b][a]==1: board[b][a]=0
                
            index += 1 + 2 * numToggle
            
            # CLOSE
            if index < len(item):
                numClose = item[index]
                for i in range(numClose):
                    a = item[index+2*i+1]
                    b = item[index+2*i+2]
                    board[b][a]=0
                index += 1 + 2 * numClose
            
            #OPEN
            if index < len(item):
                numOpen = item[index]
                for i in range(numOpen):
                    a = item[index+2*i+1]
                    b = item[index+2*i+2]
                    board[b][a]=1

# Case: chu O (Light swich) -> only close
def isNumberFour(block,x,y):
    # format: x y numClose <a,b>*numClose
    board = block.board
    for item in manaboard:
        if x== item[0] and y == item[1]:
            numClose = item[2]
            for i in range(numClose):
                bX = item[2*i+3]
                bY = item[2*i+4]
                board[bX][bY] = 0
                    
# Case: chu O (Light swich) -> T, C, O
def isNumberFive(block,x,y):
    # format: x y numToggle <a,b>*numToggle numClose <a,b>*numClose numOpen <a,b>*numOpen
    board = block.board
    for item in manaboard:
        if x== item[0] and y == item[1]:
            numToggle = item[2]
            index=2
            for i in range(numToggle):
                a = item[2*i+3]
                b = item[2*i+4]
                if board[b][a]==0: board[b][a]=1
                elif board[b][a]==1: board[b][a]=0
            index += 1 + 2 * numToggle
            if index < len(item):
                numClose = item[index]
                for i in range(numClose):
                    a = item[index+2*i+1]
                    b = item[index+2*i+2]
                    board[b][a]=0
                index += 1 + 2 * numClose
            
            #OPEN
            if index < len(item):
                numOpen = item[index]
                for i in range(numOpen):
                    a = item[index+2*i+1]
                    b = item[index+2*i+2]
                    board[b][a]=1

# Case: chu O (Light swich) -> only open
def isNumberSix(block,x,y):
    # format: x y numOpen <a,b>*numOpen
    board = block.board
    for item in manaboard:
        if x== item[0] and y == item[1]:
            numOpen = item[2]
            for i in range(numClose):
                bX = item[2*i+3]
                bY = item[2*i+4]
                board[bX][bY] = 1

# Case: SPLIT -> phan ra thanh 2 khoi
def isNumberSeven(block,x,y):  
    # format: x y numSplit <a,b>*numSplit
    board = block.board
    array = []    
    for item in manaboard:
        if x==item[0] and y==item[1]:
            numSplit = item[2]
            # format 
            for i in range(numSplit):
                a = item[2*i+3]
                b = item[2*i+4]
                array.append([a,b])

    block.y = array[0][0]
    block.x = array[0][1]
    block.y1 = array[1][0]
    block.x1 = array[1][1]
    block.rotation = "SPLIT"


# Case: chu X (Heavy swich) -> only open
def isNumberEight(block,x,y):
    # format: x y numOpen <a,b>*numOpen
    board = block.board
    for item in manaboard:
        if x== item[0] and y == item[1]:
            numOpen = item[2]
            for i in range(numClose):
                bX = item[2*i+3]
                bY = item[2*i+4]
                board[bX][bY] = 1
