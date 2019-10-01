import sys
del sys.path[0]
sys.path.insert(0, '..')

import arcade
import random
import PIL

from Elements.Element import *
from Utils.Consts import *
from Utils.Position import *

class Fire(Element):

    def __init__(self, imageName):
        super().__init__(imageName)
        self._isMortal = True
        self.DELAY_MOVIMENT = 5
        self.__countDelay = 0
