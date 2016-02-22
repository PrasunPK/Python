class ComplexNumber:
    def __init__(self,realPart,imaginaryPart):
        self.__x = realPart
        self.__y = imaginaryPart

    def add(self, other):
        return ComplexNumber(self.__x + other.__x , self.__y + other.__y)


    def getX(self):
        return self.__x

    def getY(self):
        return self.__y
