
class midtermstruct:
    def __init__(self,open1,high,low,close,volume,date):
        self.__open1=open1
        self.__high=high
        self.__low=low
        self.__close=close
        self.__volume=volume
        self.__date=date
    def getOpen(self):
        return self.__open1
    def getHigh(self):
        return self.__high
    def getLow(self):
        return self.__low
    def getClose(self):
        return self.__close
    def getVolume(self):
        return self.__volume
    def getDate(self):
        return self.__date

