import Element.py

class Fire(Element):
    
    def __init__(self, imageName):
        super().__init__(imageName)
        self._isMortal = True
        self.DELAY_MOVIMENT = 5
        self.__countDelay = 0