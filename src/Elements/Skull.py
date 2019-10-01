import Element.py

class Fire(Element):
    
    def __init__(self, imageName):
        super().__init__(imageName)
        self._isTransposable = False
        self.TIMER_FIRE = 40
        self.__contIntervals = 0