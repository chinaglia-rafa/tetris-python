import sys
del sys.path[0]
sys.path.insert(0, '..')

import arcade
import random
import PIL

from Elements.Element import *
from Utils.Consts import *
from Utils.Position import *

class Lolo(Element):
    def __init__(self, imageName):
        super().__init__(imageName)

    # def autoDraw(self, caminho):
    #     self.lolo = arcade.Sprite("/Users/seaskythe/Documents/UNESP/Segundo Ano/Segundo Semestre/POO 2/Tetris/projetotetris-programadores_do_apocalipse/OneDrive/Documentos/Dics/POO/Tetris_Alunos/imgs/lolo.png", CHARACTER_SCALING)
    #     self.lolo.center_x = 64
    #     self.lolo.center_y = 120
