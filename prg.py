class Info:
    def getRoll(self):
        return self.__roll
    def getName(self):
        return self.__name
    def setRoll(self, roll):
        self.__roll = roll
    def setName(self, name):
        self.__name = name
    
class Marks(Info):
    def __init__(self, s1, s2, s3, s4, s5):
        self.__s1=s1
        self.__s2=s2
        self.__s3=s3
        self.__s4=s4
        self.__s5=s5
        
    def getTotal(self):
        return self.__s1+self.__s2+self.__s3+self.__s4+self.__s5
        
    def getPercentage(self):
        return (self.__s1+self.__s2+self.__s3+self.__s4+self.__s5)/5
        
class Result(Marks):
    def __init__(self, name, roll, s1, s2, s3, s4, s5):
        super().__init__(s1, s2, s3, s4, s5)
        self.setName(name)
        self.setRoll(roll)
    
    def printResult(self):
        print("Name: ", self.getName())
        print("Roll: ", self.getRoll())
        print("Total: ", self.getTotal())
        print("PErcentage: ", self.getPercentage())

myStudent = Result("Ram", "999888", 95, 96, 97, 98, 99)
myStudent.printResult()
