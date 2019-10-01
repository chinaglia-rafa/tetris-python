import sys
del sys.path[0]
sys.path.insert(0, '..')

import arcade
import random
import PIL

from Elements.Element import *
from Utils.Consts import *
from Utils.Position import *
from Utils.Position import Position

class Element:
    def __init__(self, imageName):
        self._pos = Position(1, 1)
        self._isTransposable = True
        self._isMortal = False

    def overlap(self, elem):
        xDist = elem.x - self._pos.x
        yDist = elem.y - self._pos.y

        if(xDist < 1.0 and yDist < 1.0):
            return True
        else:
            return False

    def setPosition(self, x, y):
        return self._pos.setPosition

    @property
    def isTransposable(self):
        return self._isTransposable

    @property
    def isTransposable(self, isTransposable):
        self._isTransposable = isTransposable

    @property
    def isMortal(self):
        return self._isMortal

    @property
    def moveUp(self):
        return self._pos.moveUp

    @property
    def moveDown(self):
        return self._pos.moveDown

    @property
    def moveRight(self):
        return self._pos.moveRight

    @property
    def moveLeft(self):
        return self._pos.moveLeft
