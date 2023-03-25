import numpy as np

# Case 3: Chữ X
def isNumberThree(block,y,x):

    for switch in block.switches:
        if (y,x) ==  (switch[0], switch[1]):
            # TOGGLEEEE
            numToggle = switch[2]   # num toggle

            for i in range(numToggle):    # traverse toggle array
                
                bY = switch[2*i+3]
                bX = switch[2*i+4]
                if block.board[bY][bX] == 0:
                    block.board[bY][bX] = 1
                else:
                    block.board[bY][bX] = 0
                

            numCloseIndex = 2*numToggle + 3
            numClose = switch[numCloseIndex]

            for i in range(numClose):    # traverse toggle array
                bY = switch[numCloseIndex + 2*i +1]
                bX = switch[numCloseIndex + 2*i + 2]
                block.board[bY][bX] = 0
                    
            numOpenIndex = numCloseIndex + 2*numClose + 1
            numOpen = switch[numOpenIndex]
            
            for i in range(numOpen):
                bY = switch[numOpenIndex + 2*i +1]
                bX = switch[numOpenIndex + 2*i + 2]
                block.board[bY][bX] = 1
        



# Case 4: Cục tròn đặc (only đóng).
def isNumberFour(block,y,x):
    
    for switch in block.switches:
        if (y,x) ==  (switch[0], switch[1]):
            # TOGGLEEEE
            numToggle = switch[2]   # num toggle

            for i in range(numToggle):    # traverse toggle array
                bY = switch[2*i+3]
                bX = switch[2*i+4]
                if block.board[bY][bX] == 0:
                    block.board[bY][bX] = 1
                else:
                    block.board[bY][bX] = 0
            
            numCloseIndex = 2*numToggle + 3
            numClose = switch[numCloseIndex]
            
            for i in range(numClose):    # traverse toggle array
                bY = switch[numCloseIndex + 2*i +1]
                bX = switch[numCloseIndex + 2*i + 2]
                block.board[bY][bX] = 0
                    
            numOpenIndex = numCloseIndex + 2*numClose + 1
            numOpen = switch[numOpenIndex]
            
            for i in range(numOpen):
                bY = switch[numOpenIndex + 2*i +1]
                bX = switch[numOpenIndex + 2*i + 2]
                block.board[bY][bX] = 1



# Case 7: Cục phân thân
def isNumberFive(block,y,x):  

    array = []    
    for switch in block.switches:

        if (y,x) ==  (switch[0], switch[1]):
            num = switch[2]
            # format x7 y7 2 x y x1 y1
            for i in range(num):
                bY = switch[2*i+3]
                bX = switch[2*i+4]
                array.append([bY,bX])

    (block.y,block.x,block.y1,block.x1) = \
            (array[0][0],array[0][1],array[1][0], array[1][1])

    block.rotation = "SPLIT"
