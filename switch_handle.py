import numpy as np

# Case 3: Chữ X
def isNumberThree(block,y,x):

    for switch in block.switches:
        switch = np.fromstring(switch, dtype=int, sep=" ")
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
        



# Case 4: Cục tròn đặc (only đóng).
def isNumberFour(block,y,x):
    
    #print("(x-y) = (", x,"-", y,")")
    for switch in block.switches:
        switch = np.fromstring(switch, dtype=int, sep=" ")
        if (y,x) ==  (switch[0], switch[1]):
            num = switch[2]
            
            for i in range(num):
                
                bY = switch[2*i+3]
                bX = switch[2*i+4]
                block.board[bY][bX] = 0

# Case 5: Cục tròn đặc (toggle)
def isNumberFive(block,y,x):
    for switch in block.switches:
        switch = np.fromstring(switch, dtype=int, sep=" ")
        
        if (y,x) ==  (switch[0], switch[1]):
            numToggle = switch[2]     # numtoggle

            for i in range(numToggle):
                bY = switch[2*i+3]
                bX = switch[2*i+4]
                if block.board[bY][bX] == 0:
                    block.board[bY][bX] = 1
                else:
                    block.board[bY][bX] = 0


# Case 6: Cục tròn đặc (only mở)
def isNumberSix(block,y,x):

    for switch in block.switches:
        switch = np.fromstring(switch, dtype=int, sep=" ")
        if (y,x) ==  (switch[0], switch[1]):
            
            num = switch[2]
            
            for i in range(num):
                bY = switch[2*i+3]
                bX = switch[2*i+4]
                block.board[bY][bX] = 1

# Case 7: Cục phân thân
def isNumberSeven(block,y,x):  

    array = []    
    for switch in block.switches:
        switch = np.fromstring(switch, dtype=int, sep=" ") 
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

# Case 8: Chữ X (only mở)
def isNumberEight(block,y,x):

    for switch in block.switches:
        switch = np.fromstring(switch, dtype=int, sep=" ") 
        if (y,x) ==  (switch[0], switch[1]):

            num = switch[2]
            for i in range(num):
                bY = switch[2*i+3]
                bX = switch[2*i+4]
                block.board[bY][bX] = 1