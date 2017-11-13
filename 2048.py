import pyautogui, time, os, logging, sys, random, copy, math
import numpy as np
#Boarder of Board is 10
boarder=10
#Each Square is 110x110
square =110
#Class to store x and y's of detected on screen board
class tile:
    def __init__(self, x1, y1):
        self.x=x1
        self.y=y1

#Stores gameBoard information such as where numbers are and
#can manipulate the board
class gameBoard:
    def __init__(self):
        self.board = [[0 for x in range(4)] for y in range(4)]
        for x in range (0,4):
            for y in range (0,4):
                self.board[x][y] = None;
    #INCREASES VALUE OF BASE 2 EXPONENT IN DESIRED SQUARE
    def increaseValue(self, X,Y):
        if self.board[X][Y] is None:
            self.board[X][Y] = 1
        else:
            self.board[X][Y] += 1
    #BELOW ARE FUNCTIONS TO MOVE ONE SQUARE AT A TIME
    def moveOneDown(self,Y,X):
        if X < 3:
            if self.board[X][Y] == None:
                return False;
            else:
                if self.board[X+1][Y] is not None:
                    return False;
                else:
                    self.board[X+1][Y]=self.board[X][Y]
                    self.board[X][Y]=None
                    return True
        else:
            return False
        return True
    def moveOneUp(self, Y,X):
        if X > 0:
            if self.board[X][Y] == None:
                # print "HERE"
                return False;
            else:
                if self.board[X-1][Y] is not None:
                    return False;
                else:
                    self.board[X-1][Y]=self.board[X][Y]
                    self.board[X][Y]=None
                    return True
        else:
            return False
        return True
    def moveOneLeft(self, Y, X):
        if Y > 0:
            if self.board[X][Y] == None:
                return False;
            else:
                if self.board[X][Y-1] is not None:
                    return False;
                else:
                    self.board[X][Y-1]=self.board[X][Y]
                    self.board[X][Y]=None
                    return True
        else:
            return False
        return True
    def moveOneRight(self,Y,X):
        if Y < 3:
            if self.board[X][Y] == None:
                return False;
            else:
                if self.board[X][Y+1] is not None:
                    return False;
                else:
                    self.board[X][Y+1]=self.board[X][Y]
                    self.board[X][Y]=None
                    return True
        else:
            return False
        return True
    #ADDS DIRECTLY TO NEXT SQUARE IN DIRECTION INDICATED
    def addDown(self,Y):
        added = False
        for X in reversed(range (0,3)):
            if self.board[X+1][Y] is self.board[X][Y] and self.board[X][Y] is not None:
                self.increaseValue(X+1,Y)
                self.board[X][Y]=None
                added=True
                X+=1
        return added
                # return True;
    def addLeft(self,X):
        added = False
        for Y in range (0,3):
            if self.board[X][Y+1] is self.board[X][Y] and self.board[X][Y] is not None:
                self.increaseValue(X,Y)
                self.board[X][Y+1]=None
                added=True
        return added
    def addRight(self,X):
        added = False
        for Y in reversed(range(1,4)):
            if self.board[X][Y-1] is self.board[X][Y] and self.board[X][Y] is not None:
                self.increaseValue(X,Y)
                self.board[X][Y-1]=None
                added=True
        return added
    def addUp(self, Y):
        added = False
        for X in range (0,3):
            if self.board[X][Y] is self.board[X+1][Y] and self.board[X][Y] is not None:
                self.increaseValue(X,Y)
                self.board[X+1][Y]=None
                added = True
        return added
    #MOVES AN ENTIRE ROW IN INDICATED DIRECTION
    def moveUp(self, X):
        boolValid = False
        for i in range (0,3):
            for j in reversed(range (1,i+2)):
                if self.moveOneUp(X,j):
                    boolValid = True
        if self.addUp(X):
            boolValid = True
        for i in range (0,3):
            for j in reversed(range (1,i+2)):
                if self.moveOneUp(X,j):
                    boolValid = True
        return boolValid
    def moveDown(self,X):
        boolValid = False
        for a in range (0,3):
            for i in reversed(range (a,3)):
                if self.moveOneDown(X,i):
                    boolValid=True
        if self.addDown(X):
            boolValid = True
        for a in range (0,3):
            for i in reversed(range (a,3)):
                if self.moveOneDown(X,i):
                    boolValid=True
        return boolValid
    def moveLeft(self,X):
        boolValid = False
        for i in range (0,3):
            for j in reversed(range(i, 4)):
                if self.moveOneLeft(j,X):
                    boolValid=True
        if self.addLeft(X):
            boolValid=True
        for i in range (0,3):
            for j in reversed(range(i, 4)):
                self.moveOneLeft(j,X)
        return boolValid

    def moveRight(self,X):
        boolValid = False
        for i in range (0,3):
            for j in reversed(range(i, 3)):
                if self.moveOneRight(j,X):
                    boolValid=True
        if self.addRight(X):
            boolValid = True
        for i in range (0,3):
            for j in reversed(range(i, 3)):
                self.moveOneRight(j,X)
        return boolValid

    def setValue(self, X, Y, Value):
        self.board[X][Y] = int(math.log(Value,2))
    def printBoard(self):
        string = ""
        for x in range (0,4):
            string += "\n"
            for y in range(0,4):
                if self.board[x][y] is not None:
                    string += str(int(2**self.board[x][y]))
                else:
                    string += "N"
                string += " "
        return string
    #MOVES ENTIRE BOARD IN DESIRED DIRECTION
    def shiftDown(self):
        boolValid = False
        for i in range (0,4):
            if self.moveDown(i):
                boolValid=True
        return boolValid
    def shiftUp(self):
        boolValid = False
        for i in range(0,4):
            if self.moveUp(i):
                boolValid=True
        return boolValid
    def shiftLeft(self):
        boolValid = False
        for i in range(0,4):
            if self.moveLeft(i):
                boolValid=True
        return boolValid
    def shiftRight(self):
        boolValid = False
        for i in range (0,4):
            if self.moveRight(i):
                boolValid=True
        return boolValid
    def clone(self):
        return self
    #SCORES BOARD WITH RESPECT TO TEXT FILE GENERATED IN C++
    def scoreCurrentBoard(self):
        score = 0
        #ADDS UP ROWS
        for i in range (0,4):
            a=self.board[i][0]
            if a is None:
                a = 0
            b=self.board[i][1]
            if b is None:
                b = 0
            c=self.board[i][2]
            if c is None:
                c = 0
            d=self.board[i][3]
            if d is None:
                d = 0
            score += (table[int(a),int(b),int(c),int(d)])
        #ADDS UP ROWS
        for i in range (0,4):
            a=self.board[0][i]
            if a is None:
                a = 0
            b=self.board[1][i]
            if b is None:
                b = 0
            c=self.board[2][i]
            if c is None:
                c = 0
            d=self.board[3][i]
            if d is None:
                d = 0
            score += (table[int(a),int(b),int(c),int(d)])
        #RETURN TOTAL
        return score
    #Inserts Tile Into Board
    def insert(self, num, val):
        if self.board[num/4][num%4] is None:
            self.setValue(num/4,num%4, val)
            return True
        return False
    #RETURNS TRUE IF SQUARE IS EMPTY
    def empty(self, num):
        if self.board[num/4][num%4] is None:
            return True
        return False
    #DEFINES MOVEMENT OF BOARD TO 1,2,3,4 FOR AI
    def moveBoard(self, id):
        if id is 0:
            return self.shiftLeft()
        elif id is 1:
            return self.shiftUp()
        elif id is 2:
            return self.shiftRight()
        elif id is 3:
            return self.shiftDown()
    #INSERTS A RANDOM TILE FOR TESTING PURPOSES, NOT CALLED IN FINAL VERSION
    def randomTile(self):
        arr = np.zeros((16))
        index = 0
        for i in range (0,16):
            if self.empty(i):
                arr[index] = i
                index+=1
        a = random.randint(0,index-1)
        b = 2
        if random.randint(0,9) is 9:
            b = 4
        self.insert(int(arr[a]), b)


#CLASS TO CONTROL MOVES DICTATED BY PROGRAM
class AI:
    def __init__ (self):
        return None

    def makeMove(self, id):
        if id is 0:
            pyautogui.press('a')
        elif id is 1:
            pyautogui.press('w')
        elif id is 2:
            pyautogui.press('d')
        elif id is 3:
            pyautogui.press('s')
        game.moveBoard(id)
        temp=copy.deepcopy(game)
        #MUST SLEEP SO SQUARE CAN SHOW UP ON BOARD AND TAKE ACCURATE READS OF COLOR
        time.sleep(.2)
        for i in range (0,16):
            if temp.empty(i):
                if checkSquare(i/4,i%4):
                    break
    #BASIC EXPECTIMAX SEARCH
    #MUST WAY CHANCE OF 2's AND 4's
    #.9 CHANCE FOR 2
    #.1 CHANCE FOR 4
    def expectimax(self, depth, id, temp):
        if depth is 0:
            return temp.scoreCurrentBoard()
        #IF ID IS 0 IT IS TURN TO GENERATE RANDOM TILE
        elif id is 0:
            score = 0
            count = 0
            for i in range (0,16):
                if temp.empty(i):
                    newTemp = gameBoard()
                    newTemp=copy.deepcopy(temp)
                    newTemp.insert(i,2)
                    #BRANCH FOR 2
                    score += .9*self.expectimax(depth-1, 1, newTemp)
                    newTemp=copy.deepcopy(temp)
                    newTemp.insert(i, 4)
                    #BRANCH FOR 4
                    score+=.1*self.expectimax(depth-1, 1, newTemp)
                    count+=1
            return score/count
        #IF ID IS 1 IT IS THE TURN OF THE AI
        elif id is 1:
            score = 0
            moveBool = False
            for i in range (0,4):
                newTemp = gameBoard()
                newTemp=copy.deepcopy(temp)
                if newTemp.moveBoard(i):
                    score = max(score, self.expectimax(depth-1, 0,newTemp))
                    moveBool=True
            #IF NO MOVES WORK, GAME IS OVER, RETURN VERY LOW SCORE
            if not moveBool:
                return -10000
            return score
    #FUNCTION THAT CALLS EXPCTIMAX ORIGINALLY AND RETURNS BEST MOVE
    def getBestMove(self,depth):
        score = float('-inf')
        bestMove=0
        # print "IN BEST MOVE"
        for i in range (0,4):
            # print (i, "MOVE DONE")
            newTemp = gameBoard()
            newTemp = copy.deepcopy(game)
            if (newTemp.moveBoard(i)):
                newScore = self.expectimax(depth-1, 0, newTemp)
                if (newScore>score):
                    bestMove=i
                    score = newScore

        return bestMove
    #CHECKS IF MOVE IS POSSIBLE
    def canMakeMove(self):
        boolVal = False
        for i in range (0,4):
            temp = copy.deepcopy(game)
            if temp.moveBoard(i):
                boolVal = True
                break
        return boolVal


#GET LOCATION OF BOARD ON SCREEN IN COMPARISON TO IMAGE STORED
def getGameRegion():
    region = pyautogui.locateCenterOnScreen("./2048IMAGES/TOPLEFT.png")
    x,y=region
    global Game_Region
    Game_Region = (x, y, 500, 500)

#ADDS TEXT FILE GENERATED IN C++ AS A TABLE TO SCORE BOARD FROM
def getTable():
    power = 17
    global table
    table = np.zeros((power,power,power,power))
    fileName = "./Cases.txt"
    tableFile = open(fileName, 'r')
    lineNumber=1;
    for i in range (0,power):
        for j in range (0,power):
            for k in range (0,power):
                for l in range (0,power):
                    table[i,j,k,l]=tableFile.readline()
#FIND X,Y OF SPECIFIC SQUARES ON BOARD AND STORE IN AN ARRAY
def findTiles():
    region = (Game_Region[0]+boarder,Game_Region[1]+boarder,square,square)
    n=0
    global tiles
    tiles = [[0 for x in range(4)] for y in range(4)]
    tiles [0][0] = tile(Game_Region[0]+boarder,Game_Region[1]+boarder)
    XVAL1 = Game_Region[0]+boarder
    YVAL1 = Game_Region[1]+boarder
    for i in range(0,4):
        YVAL = YVAL1+i*(boarder+square)
        for j in range(0,4):
            XVAL = XVAL1+j*(boarder+square)
            tiles[i][j] = tile(XVAL, YVAL)
#CHECKS FOR AN ADDED SQUARE OF 2 OR 4 AT THE SPECIFICIED LOCATION AND SETS THAT VALUE INTERNALLY
def checkSquare(x,y):
    #COLOR FOR 2
    if pyautogui.pixelMatchesColor(tiles[x][y].x+20, tiles[x][y].y+20, (239, 219, 185)):
        game.setValue(x,y,2)
        return True
        # print "2"
    #COLOR FOR 4
    elif pyautogui.pixelMatchesColor(tiles[x][y].x+20, tiles[x][y].y+20, (239, 215, 170)):
        game.setValue(x,y,4)
        return True
        # print '4'
    return False
#CHECKS COLLUMN BY COLLUMN
#NEVER CALLED
def checkCollumn(x):
    for i in range (0,4):
        checkSquare(x,i)
#CHECKS ROW BY ROW
def checkRow(y):
    for i in range(0,4):
        checkSquare(i,y)
#USED TO SET INITIAL GAMEBOARD
def setBoardStart():
    for i in range (0,4):
        checkRow(i)
#CALLED FIRST TO CALL ALL NECESSARY FUCNTIONS IN THE REQUIRED ORDER TO RUN THE GAME
def initialize():
    global game
    game = gameBoard()
    getGameRegion()
    findTiles()
    setBoardStart()
    getTable()
#FOR TESTING PURPOSES
def initializeLocal():
    global game
    game = gameBoard()
    getTable()

def main():
    initialize()
    print "BOARD INITIALIZED"
    bot = AI()
    print "AI INITIALIZED"
    while bot.canMakeMove():
        a = bot.getBestMove(2)
        bot.makeMove(a)
        print game.printBoard()
    print'\n'
    print "GAMEOVER"

#CALL TO MAIN
main()
