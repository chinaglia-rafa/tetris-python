from .Consts import Consts

class Position:

    def __init__(self, x ,y):
        self.setPosition(x, y)

    def setPosition(self, x, y):
        if(x < 0 or x > Consts.NUM_CELLS-1):
            return False;
        self.__previousx = self.__x
        self.__x = x;
        
        if(y < 0 or y > Consts.NUM_CELLS-1):
            return False;
        self.__previousy = self.__y;
        self.__y = y;
        return True

    @property
    def moveUp(self):
        return self.setPosition(self.__x, self.__y+1)

    @property
    def moveDown(self):
        return self.setPosition(self.__x, self.__y-1)
    
    @property
    def moveRight(self):
        return self.setPosition(self.__x+1, self.__y)

    @property
    def moveLeft(self):
        return self.setPosition(self.__x-1, self.__y)

    @property
    def comeBack(self):
        return self.setPosition(self.__previousx, self.__previousy)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y