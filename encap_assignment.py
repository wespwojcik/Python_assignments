




class Protected:
    def __init__(self):
        self.__privateVar = 12

    def getprivate(self):
        print(self.__privateVar)

    def setprivate(self,private):
        self.__privateVar = private

obj = Protected()
obj.getprivate()
obj.setprivate(45)
obj.getprivate()
